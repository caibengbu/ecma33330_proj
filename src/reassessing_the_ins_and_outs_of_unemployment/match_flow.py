import pandas as pd
from .other_utils import get_merged_pickle_filename, months_interval, pairwise

def match_flow(date1,date2,theDir):
    filename = get_merged_pickle_filename(theDir,date1,date2)
    df = pd.read_pickle(filename)
    df = df[df.age >=16]

    status_dict_pre198901 = {
        1.0: "E",
        2.0: "E",
        3.0: "U",
        4.0: "I",
        5.0: "I",
        6.0: "I",
        7.0: "I"
    }

    status_dict_post198901 = {
        1.0: "E",
        2.0: "E",
        3.0: "U",
        4.0: "U",
        5.0: "I",
        6.0: "I",
        7.0: "I"
    }

    if date1 > "198900":
        first_dict = status_dict_post198901
    else:
        first_dict = status_dict_pre198901

    if date2 > "198900":
        second_dict = status_dict_post198901
    else:
        second_dict = status_dict_pre198901

    df['lfs_x'] = df.status_x.map(first_dict).fillna('M')
    df['lfs_y'] = df.status_y.map(second_dict).fillna('M')
    df['direction'] = df['lfs_x'] + df['lfs_y']
    df['weight'] = (df['fweight_x'].fillna(0) + df['fweight_y'].fillna(0))/2
    df2 = df.groupby('direction').agg({'weight': 'sum'})
    flows_dict = df2.to_dict('index')

    if 'EE' in flows_dict:
        ttlflow_fromE = flows_dict['EE']['weight']+flows_dict['EI']['weight']+flows_dict['EU']['weight']+flows_dict['EM']['weight']
        ttlflow_fromU = flows_dict['UE']['weight']+flows_dict['UI']['weight']+flows_dict['UU']['weight']+flows_dict['UM']['weight']
        ttlflow_fromI = flows_dict['IE']['weight']+flows_dict['II']['weight']+flows_dict['IU']['weight']+flows_dict['IM']['weight']
        ttlflow_fromM = flows_dict['ME']['weight']+flows_dict['MI']['weight']+flows_dict['MU']['weight']
        flowEE = flows_dict['EE']['weight']/ttlflow_fromE
        flowEI = flows_dict['EI']['weight']/ttlflow_fromE
        flowEU = flows_dict['EU']['weight']/ttlflow_fromE
        flowEM = flows_dict['EM']['weight']/ttlflow_fromE
        flowUE = flows_dict['UE']['weight']/ttlflow_fromU
        flowUI = flows_dict['UI']['weight']/ttlflow_fromU
        flowUU = flows_dict['UU']['weight']/ttlflow_fromU
        flowUM = flows_dict['UM']['weight']/ttlflow_fromU
        flowIE = flows_dict['IE']['weight']/ttlflow_fromI
        flowII = flows_dict['II']['weight']/ttlflow_fromI
        flowIU = flows_dict['IU']['weight']/ttlflow_fromI
        flowIM = flows_dict['IM']['weight']/ttlflow_fromI
        flowME = flows_dict['ME']['weight']/ttlflow_fromM
        flowMI = flows_dict['MI']['weight']/ttlflow_fromM
        flowMU = flows_dict['MU']['weight']/ttlflow_fromM
        
        return [date2,flowEE,flowEI,flowEU,flowEM,flowUE,flowUI,flowUU,flowUM,flowIE,flowII,flowIU,flowIM,flowME,flowMI,flowMU]
    else:
        return [date2,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None]

def flow_all(start_date,end_date,theDir):
    dates = months_interval(start_date,end_date)
    data = []
    for date1,date2 in pairwise(dates):
        print(f"creating flow between {date1} and {date2}")
        data.append(match_flow(date1,date2,theDir))
    date,flowsEE,flowsEI,flowsEU,flowsEM,flowsUE,flowsUI,flowsUU,flowsUM,flowsIE,flowsII,flowsIU,flowsIM,flowsME,flowsMI,flowsMU = zip(*data)
    df = pd.DataFrame({'date': date,
                  'flowEE':flowsEE,
                  'flowEI':flowsEI,
                  'flowEU':flowsEU,
                  'flowEM':flowsEM,
                  'flowUE':flowsUE,
                  'flowUI':flowsUI,
                  'flowUU':flowsUU,
                  'flowUM':flowsUM,
                  'flowIE':flowsIE,
                  'flowII':flowsII,
                  'flowIU':flowsIU,
                  'flowIM':flowsIM,
                  'flowME':flowsME,
                  'flowMI':flowsMI,
                  'flowMU':flowsMU})
    return df

        

