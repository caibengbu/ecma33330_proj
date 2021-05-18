import requests
import json
import numpy as np
import sys

def retrieve(request_range):
    res_dict = {'LNS13000000': None,
            'LNS12000000': None,
            'LNS13008396': None}
    start_year = str(request_range[0])
    end_year = str(request_range[-1])
    headers = {'Content-type': 'application/json'}
    data = json.dumps({"seriesid": ['LNS13000000','LNS12000000','LNS13008396'],"startyear":start_year, "endyear":end_year})
    p = requests.post('https://api.bls.gov/publicAPI/v2/timeseries/data/', data=data, headers=headers)
    json_data = json.loads(p.text)
    if json_data['Results'] != {}:
        for series in json_data['Results']['series']:
            seriesId = series['seriesID']
            x = []
            for item in series['data']:
                year = item['year']
                period = item['period'][1:3]
                value = item['value']
                footnotes=""
                for footnote in item['footnotes']:
                    if footnote:
                        footnotes = footnotes + footnote['text'] + ','
                if '01' <= period <= '12':
                    x.append([year+period,value])
            x = np.array(x)
            res_dict[seriesId] = x
        return res_dict
    else:
        raise NameError('Retrieve Not Successful')

start_date = sys.argv[1]
end_date = sys.argv[2]
start_year = int(start_date[0:4])
end_year = int(end_date[0:4])
year_range = np.arange(start_year,end_year+1)
request_times = len(year_range) // 10 + 1
request_range_pertime = np.array_split(year_range,request_times)

res = {'LNS13000000': [None,None],
        'LNS12000000': [None,None],
        'LNS13008396': [None,None]}

for theRange in request_range_pertime:
    res_temp_dict = retrieve(theRange)
    for keyID in res:
        res[keyID] = np.vstack((res[keyID],res_temp_dict[keyID]))

for keyID in res:
    data = res[keyID].astype("float64")
    data_sorted = data[np.argsort(data[:,0])]
    selected = (data_sorted[:,0] >= int(start_date)) & (data_sorted[:,0] <= int(end_date))
    np.savetxt("../output/"+keyID+".txt",data_sorted[selected,:])