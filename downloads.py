import urllib.request
import sys
from zipfile import ZipFile
import os

start_year = int(sys.argv[1][0:4])
start_month = int(sys.argv[1][4:6])

end_year = int(sys.argv[2][0:4])
end_month = int(sys.argv[2][4:6])

months = ["jan", "feb", "mar", "apr", "may", "jun",
          "jul", "aug", "sep", "oct", "nov", "dec"]
months_num = [str(i+1).zfill(2) for i in range(12)]
month_dict = dict(zip(months_num, months))

def months_inteval(start_year, start_month, end_year, end_month):
    if start_year==end_year:
        return [str(start_year)+str(month).zfill(2) for month in range(start_month,end_month+1)]
    else:
        months_in_start_year = [str(start_year)+str(month).zfill(2) for month in range(start_month,13)]
        months_in_end_year = [str(end_year)+str(month).zfill(2) for month in range(1,end_month+1)]
        months_in_between = [str(year) + month for month in months_num for year in range(start_year+1, end_year)]
        return months_in_start_year + months_in_between + months_in_end_year

date_list = months_inteval(start_year, start_month, end_year, end_month)
for date in date_list:
    print("Prepare to download CPS file for " + date + " ...")
    year = date[2:4]
    month = date[4:6]
    filename = month_dict[month] + year + "pub.zip"
    url = 'https://data.nber.org/cps-basic/' + filename
    print("Downloading CPS file for " + date + " ...")
    urllib.request.urlretrieve(url, filename)
    print("Download finished")
    with ZipFile(filename, 'r') as zip:
        content_name = zip.namelist()[0]
        content_file_extention = os.path.splitext(content_name)[1]
        print('Extracting all the files now ...') 
        zip.extractall()
    print("Cleaning .zip file ...")
    os.remove(filename)
    os.rename(content_name, date+content_file_extention)
    print("Download for " + date + " is completed!")

