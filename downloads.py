import urllib.request
import sys
from zipfile import ZipFile
import os
import shutil

# The starting year of the period of which we want to download data
start_year = int(sys.argv[1][0:4]) 
# The starting month of the period of which we want to download data
start_month = int(sys.argv[1][4:6]) 

# The ending year of the period of which we want to download data
end_year = int(sys.argv[2][0:4]) 
# The ending month of the period of which we want to download data
end_month = int(sys.argv[2][4:6])

months = ["jan", "feb", "mar", "apr", "may", "jun",
          "jul", "aug", "sep", "oct", "nov", "dec"]
months_num = [str(i+1).zfill(2) for i in range(12)]
month_dict = dict(zip(months_num, months)) # Create a "month number -> month abbr" dictionary

def months_inteval(start_year, start_month, end_year, end_month):
    # This function retruns all the months in the form of YYYYMM, within the rage of starting date and ending date.
    if start_year==end_year:
        return [str(start_year)+str(month).zfill(2) for month in range(start_month,end_month+1)]
    else:
        months_in_start_year = [str(start_year)+str(month).zfill(2) for month in range(start_month,13)]
        months_in_end_year = [str(end_year)+str(month).zfill(2) for month in range(1,end_month+1)]
        months_in_between = [str(year) + month for month in months_num for year in range(start_year+1, end_year)]
        return months_in_start_year + months_in_between + months_in_end_year

theDir = "cpsbasic_data/"
if os.path.exists(theDir):
    shutil.rmtree(theDir)
os.makedirs(theDir)

date_list = months_inteval(start_year, start_month, end_year, end_month) # Get all the wanted months in the list
for date in date_list:
    # Iterate through the list to download all the corresponding data
    print("Prepare to download CPS file for " + date + " ...")
    year = date[2:4]
    month = date[4:6]
    filename = theDir + month_dict[month] + year + "pub.zip" # Generate the filename in line with data.nber.org
    url = 'https://data.nber.org/cps-basic/' + month_dict[month] + year + "pub.zip"
    print("Downloading CPS file for " + date + " ...")
    urllib.request.urlretrieve(url, filename) # Download the zip file
    print("Download finished")
    with ZipFile(filename, 'r') as zip:
        content_name = zip.namelist()[0] # Gets the name of data file inside downloaded zip file
        content_file_extention = os.path.splitext(content_name)[1] # Gets the data file extension
        print('Extracting all the files now ...') 
        zip.extractall(path=theDir) # Extracting the data
    print("Cleaning .zip file ...")
    os.remove(filename) # Remove the zip file
    os.rename(theDir+content_name, theDir+date+content_file_extention) # Rename the data file
    print("Download for " + date + " is completed!")

