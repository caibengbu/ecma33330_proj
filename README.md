# Replicating Shimer (2012)

This repository manages codes for replicating “Reassessing the Ins and Outs of Unemployment” (Shimer, 2012), and extends the framework using the latest data during the Covid-19 pandemic.

## How to run the package
First, install the package by pip
```
pip install git+https://github.com/caibengbu/ecma33330_proj.git
```
After it is installed, simply run
```
python -m reassessing_the_ins_and_outs_of_unemployment --start_date=197601 --end_date=202110
```
This command activates an analysis from January 1976 to October 2021. You can input any interval as long as there is raw data.

You can also specify working directory by passing the `--dir` argument
```
python -m reassessing_the_ins_and_outs_of_unemployment --start_date=197601 --end_date=202110 --dir=path/to/wd
```

## Sources of Raw Data
There are two sources of raw CPS Basic Monthly data: [NBER.org](https://data.nber.org/cps-basic2/) and [Census.gov](https://www.census.gov/data/datasets/time-series/demo/cps/cps-basic.html). We made available 3 possible solutions that our users can choose from:
1. Download from NBER.org
2. Download from Census.gov
3. Download from a mixture of NBER.org (for files earlier than 1994) and Census.gov (for files later than 1994). 

Since [Census.gov](https://www.census.gov/data/datasets/time-series/demo/cps/cps-basic.html) does not support downloading data files older than 1994 but is more up-to-date than [NBER.org](https://data.nber.org/cps-basic2/) in terms of newly published data, we suggest using the third method.

## Environment and Prerequisite Installations
This package is built on and tested on Python 3.6.
