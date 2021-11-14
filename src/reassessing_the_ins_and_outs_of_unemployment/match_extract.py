import pandas as pd
import string
import os
import numpy as np
from .other_utils import months_interval, get_raw_filename, get_extracted_pickle_filename

def match_extract(date,theDir):
    print("extracting data from raw (" + date +")")
    filename = get_raw_filename(theDir,date)
    date = int(date)

    hrsersuf_dict = dict(zip(string.ascii_uppercase, range(1,27)))
    hrsersuf_dict['-1'] = 0
    hrsersuf_dict['Z'] = 25
    hrsersuf_dict['Y'] = 26

    if date <= 197712:
        data_dict = {
            "hh": (3,8),
            "hh1": (8,12),
            "hh2": (24,26),
            "line": (93,95),
            "mis": (1,2),
            "age": (96,98),
            "race": (99,100),
            "sex": (100,101),
            "status": (108,109),
            "dur": (65,67),
            "fweight": (120,132),
            "educ": (102,104),
            "grade": (104,105),
            "mar": (98,99),
            "ind": (87,90),
            "occu": (90,93)}
        df = pd.read_fwf(filename,colspecs=list(data_dict.values()),header=None)
        df.columns = list(data_dict.keys())
        df = df.replace('[^0-9]', np.nan, regex=True).astype("float64")
        df['hh3'] = df['hh']*1000000 + df['hh1']*100 + df['hh2']
        df['educ1'] = df['educ'] - df['grade'] + 1
        df = df.drop(['hh','hh1','hh2','educ'], axis=1)
        df = df.rename(columns={'hh3':'hh','educ1':'educ'})
    elif date <= 198212:
        data_dict = {
            "hh": (3,15),
            "line": (93,95),
            "mis": (1,2),
            "age": (96,98),
            "race": (99,100),
            "sex": (100,101),
            "status": (108,109),
            "dur": (65,67),
            "fweight": (120,132),
            "educ": (102,104),
            "grade": (104,105),
            "mar": (98,99),
            "ind": (87,90),
            "occu": (90,93)}
        df = pd.read_fwf(filename,colspecs=list(data_dict.values()),header=None)
        df.columns = list(data_dict.keys())
        df = df.replace('[^0-9]', np.nan, regex=True).astype("float64")
        df['educ1'] = df['educ'] - df['grade'] + 1
        df = df.drop(['educ'], axis=1)
        df = df.rename(columns={'educ1':'educ'})
    elif date <= 198312:
        data_dict = {
            "hh": (3,15),
            "line": (93,95),
            "mis": (1,2),
            "age": (96,98),
            "race": (99,100),
            "sex": (100,101),
            "status": (108,109),
            "dur": (65,67),
            "fweight": (120,132),
            "educ": (102,104),
            "grade": (104,105),
            "mar": (98,99),
            "ind": (523,526),
            "occu": (526,529)}
        df = pd.read_fwf(filename,colspecs=list(data_dict.values()),header=None)
        df.columns = list(data_dict.keys())
        df = df.replace('[^0-9]', np.nan, regex=True).astype("float64")
        df['educ1'] = df['educ'] - df['grade'] + 1
        df = df.drop(['educ'], axis=1)
        df = df.rename(columns={'educ1':'educ'})
    elif date <= 198812:
        data_dict = {
            "hh": (3,15),
            "line": (540,542),
            "mis": (1,2),
            "age": (96,98),
            "race": (99,100),
            "sex": (100,101),
            "status": (108,109),
            "dur": (65,67),
            "fweight": (120,132),
            "educ": (102,104),
            "grade": (104,105),
            "mar": (98,99),
            "ind": (523,526),
            "occu": (526,529)}
        df = pd.read_fwf(filename,colspecs=list(data_dict.values()),header=None)
        df.columns = list(data_dict.keys())
        df = df.replace('[^0-9]', np.nan, regex=True).astype("float64")
        df['educ1'] = df['educ'] - df['grade'] + 1
        df = df.drop(['educ'], axis=1)
        df = df.rename(columns={'educ1':'educ'})
    elif date <= 199112:
        data_dict = {
            "hh":(144,156),
            "line":(263,265),
            "mis":(69,70),
            "age":(269,271),
            "race":(279,280),
            "sex":(274,275),
            "status":(347,348),
            "dur":(303,305),
            "fweight":(397,405),
            "lweight":(575,583),
            "llind":(583,584),
            "educ":(276,278),
            "grade":(278,279),
            "mar":(271,272),
            "ind":(310,312),
            "occu":(313,315)}
        df = pd.read_fwf(filename,colspecs=list(data_dict.values()),header=None)
        df.columns = list(data_dict.keys())
        df = df.replace('[^0-9]', np.nan, regex=True).astype("float64")
        df['educ1'] = df['educ'] - df['grade'] + 1
        df = df.drop(['educ'], axis=1)
        df = df.rename(columns={'educ1':'educ'})
    elif date <= 199312:
        data_dict = {
            "hh":(144,156),
            "line":(263,265),
            "mis":(69,70),
            "age":(269,271),
            "race":(279,280),
            "sex":(274,275),
            "status":(347,348),
            "dur":(303,305),
            "fweight":(397,405),
            "lweight":(575,583),
            "llind":(583,584),
            "educ":(276,278),
            "mar":(271,272),
            "ind":(309,312),
            "occu":(312,315)}
        df = pd.read_fwf(filename,colspecs=list(data_dict.values()),header=None)
        df.columns = list(data_dict.keys())
        df = df.replace('[^0-9]', np.nan,regex=True).astype("float64")
    elif date <= 199505:
        data_dict = {
            "gestfips":(92,94),
            "hrhhid":(0,12),
            "hrsersuf":(74,76),
            "line":(146,148),
            "mis":(62,64),
            "age":(121,123),
            "race":(138,140),
            "sex":(128,130),
            "status":(179,181),
            "dur":(406,409),
            "fweight":(612,622),
            "lweight":(592,602),
            "llind":(68,70),
            "educ":(136,138),
            "mar":(124,126),
            "ind":(435,438),
            "occu":(438,441)}
        df = pd.read_fwf(filename,colspecs=list(data_dict.values()),header=None)
        df.columns = list(data_dict.keys())
        z = df.hrsersuf.map(hrsersuf_dict).fillna(0)
        df['z'] = pd.to_numeric(df['hrsersuf'],errors='coerce').fillna(0)
        df['z'] = df['z'] + z
        df = df.replace('[^0-9]', np.nan, regex=True).astype("float64")
        df['hh'] = df['hrhhid']*100 + df['z']
        df = df.drop(['hrhhid','hrsersuf'],axis=1)
    elif date <= 200212:
        data_dict = {
            "hrhhid":(0,15),
            "hrsersuf":(74,76),
            "line":(146,148),
            "mis":(62,64),
            "age":(121,123),
            "race":(138,140),
            "sex":(128,130),
            "status":(179,181),
            "dur":(406,409),
            "fweight":(612,622),
            "lweight":(592,602),
            "llind":(68,70),
            "educ":(136,138),
            "mar":(124,126),
            "ind":(435,438),
            "occu":(438,441)}
        df = pd.read_fwf(filename,colspecs=list(data_dict.values()),header=None)
        df.columns = list(data_dict.keys())
        z = df.hrsersuf.map(hrsersuf_dict).fillna(0)
        df['z'] = pd.to_numeric(df['hrsersuf'],errors='coerce').fillna(0)
        df['z'] = df['z'] + z
        df = df.replace('[^0-9]', np.nan, regex=True).astype("float64")
        df['hh'] = df['hrhhid']*100 + df['z']
        df = df.drop(['hrhhid','hrsersuf'],axis=1)
    else :
        data_dict = {
            "hrhhid":(0,15),
            "hrsersuf":(74,76),
            "line":(146,148),
            "mis":(62,64),
            "age":(121,123),
            "race":(138,140),
            "sex":(128,130),
            "status":(179,181),
            "dur":(406,409),
            "fweight":(612,622),
            "lweight":(592,602),
            "llind":(68,70),
            "educ":(136,138),
            "mar":(124,126),
            "ind":(855,859),
            "occu":(859,863)}
        df = pd.read_fwf(filename,colspecs=list(data_dict.values()),header=None)
        df.columns = list(data_dict.keys())
        z = df.hrsersuf.map(hrsersuf_dict).fillna(0)
        df['z'] = pd.to_numeric(df['hrsersuf'],errors='coerce').fillna(0)
        df['z'] = df['z'] + z
        df = df.replace('[^0-9]', np.nan, regex=True).astype("float64")
        df['hh'] = df['hrhhid']*100 + df['z']
        df = df.drop(['hrhhid','hrsersuf'],axis=1)

    df.to_pickle(get_extracted_pickle_filename(theDir,date))

def extract_all(start_date,end_date,theDir):
    dates = months_interval(start_date,end_date)
    for date in dates:
        filename = get_extracted_pickle_filename(theDir,date)
        if os.path.isfile(filename):
            print(f"data for {date} is already extracted")
        else:
            match_extract(date,theDir)

def clean_all_extracted(start_date,end_date,theDir):
    dates = months_interval(start_date,end_date)
    for date in dates:
        filename = get_extracted_pickle_filename(theDir,date)
        if os.path.isfile(filename):
            os.remove(filename)
