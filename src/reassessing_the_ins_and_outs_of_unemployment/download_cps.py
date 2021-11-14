import urllib.request 
import requests
from zipfile import ZipFile 
import os
import time
from .other_utils import months_interval, get_raw_filename, get_tmp_filename

months = ["jan", "feb", "mar", "apr", "may", "jun",
            "jul", "aug", "sep", "oct", "nov", "dec"]
months_num = [str(i+1).zfill(2) for i in range(12)]
month_dict = dict(zip(months_num, months))

def download_cps_single(date,theDir):
    """
    Download the CPS data from either Census or NBER.
    """
    tmp_year_str = date[0:4]
    tmp_month_str = date[4:6]
    filename_stem = month_dict[tmp_month_str]+tmp_year_str[2:4]
    if int(tmp_year_str) >= 1994:
        # Download from census if it later than 1994 
        filename = get_tmp_filename(theDir,f"tmp{date}.zip")
        url = f"https://www2.census.gov/programs-surveys/cps/datasets/{tmp_year_str}/basic/{filename_stem}pub.zip"
        print("Downloading CPS file for " + date + " from CENSUS ...")
        urllib.request.urlretrieve(url, filename)
        print("Unzipping ...")
        with ZipFile(filename , 'r') as zip:
            content_name = zip.namelist()[0]
            zip.extractall(path=os.path.join(theDir,'tmp'))
        os.remove(filename)
        os.rename(os.path.join(theDir,'tmp',content_name),get_raw_filename(theDir,date))
    else:
        # Download from NBER otherwise
        filename = get_raw_filename(theDir,date)
        url = f"https://data.nber.org/cps-basic2/raw/cpsb{date}.raw"
        print("Downloading CPS file for " + date + " from NBER ...")
        urllib.request.urlretrieve(url, filename)

def download_cps(start_date, end_date, theDir):
    """
    Download the CPS data ranging from start_date to end_date.
    """
    if not os.path.exists(theDir):
        os.makedirs(theDir)
    date_list = months_interval(start_date, end_date)
    for date in date_list:
        # Iterate through the list to download all the corresponding data
        if check_if_successfully_downloaded(theDir,date):
            if int(date) < 199401:
                time.sleep(10) # sleep for 10 second to avoid being banned by NBER
            else:
                pass
        else:
            download_cps_single(date,theDir)

def gen_url_from_date(date):
    tmp_year_str = date[0:4]
    tmp_month_str = date[4:6]
    filename_stem = month_dict[tmp_month_str]+tmp_year_str[2:4]
    if int(tmp_year_str) >= 1994:
        return f"https://www2.census.gov/programs-surveys/cps/datasets/{tmp_year_str}/basic/{filename_stem}pub.zip"
    else:
        return f"https://data.nber.org/cps-basic2/raw/cpsb{date}.raw"

def check_if_successfully_downloaded(theDir,date):
    """
    Check if a file is successfully downloaded, without interruption and corruption. 
    We check if the raw file corresponds to the size from the http request.
    If the records don't match, we might have an incomplete download.
    For data later than 1994, the downloaded file is a zip file.
    We only check if the raw file exist to infer the completion of the download.
    """
    print(f"checking if data for {date} is successfully downloaded ...")
    local = get_raw_filename(theDir,date)
    if int(date) < 199401:
        link = gen_url_from_date(date)
        if os.path.isfile(local):
            response = requests.head(link)
            if response.status_code==200:
                url_size = response.headers.get('content-length', -1)
            else:
                raise TimeoutError("Unsuccessful http request")
            local_size = os.stat(local).st_size
            if int(url_size) == local_size:
                print("it is complete! move on to next step ...")
                return True
            else:
                print("not complete! start downloading ...")
                return False
        else:
            print("didn't find any local file. start downloading ...")
            return False
    else:
        if os.path.isfile(local):
            print("it is complete! move on to next step ...")
            return True
        else:
            print("not complete! start downloading ...")
            return False

        
        
