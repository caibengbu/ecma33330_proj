import os
from itertools import tee

def months_interval(start_date, end_date):
    """
    Generate the monthly intervals between a start date and an end date
    """
    months_num = [str(i+1).zfill(2) for i in range(12)]
    start_year = int(start_date[0:4])
    start_month = int(start_date[4:6])
    end_year = int(end_date[0:4])
    end_month = int(end_date[4:6])
    if start_year==end_year:
        return [str(start_year)+str(month).zfill(2) for month in range(start_month ,end_month+1)]
    else:
        months_in_start_year = [str(start_year)+str(month).zfill(2) for month in range(start_month ,13)]
        months_in_end_year = [str(end_year)+str(month).zfill(2) for month in range(1,end_month+1)]
        months_in_between = [str(year) + month for year in range(start_year+1, end_year) for month in months_num ]
        return months_in_start_year + months_in_between + months_in_end_year

def get_raw_filename(theDir,date):
    path = os.path.join(theDir,'raw')
    if os.path.exists(path):
        pass
    else:
        os.mkdir(path)
    return os.path.join(path,f"cpsb{date}.raw")

def get_tmp_filename(theDir,real_name):
    path = os.path.join(theDir,'tmp')
    if os.path.exists(path):
        pass
    else:
        os.mkdir(path)
    return os.path.join(path,real_name)

def get_extracted_pickle_filename(theDir,date):
    path = os.path.join(theDir,'tmp')
    if os.path.exists(path):
        pass
    else:
        os.mkdir(path)
    return os.path.join(path,f"tmp_extracted_{date}.pickle")

def get_merged_pickle_filename(theDir,date1,date2):
    path = os.path.join(theDir,'tmp')
    if os.path.exists(path):
        pass
    else:
        os.mkdir(path)
    return os.path.join(path,f"tmp_merged_{date1}_{date2}.pickle")

def get_figures_filename(theDir,figname):
    path = os.path.join(theDir,'figures')
    if os.path.exists(path):
        pass
    else:
        os.mkdir(path)
    return os.path.join(path,figname)

def get_output_filename(theDir,output_name):
    path = os.path.join(theDir,'output')
    if os.path.exists(path):
        pass
    else:
        os.mkdir(path)
    return os.path.join(path,output_name)

def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)