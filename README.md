# Replicating Shimer (2012)

This repository manages codes for replicating “Reassessing the Ins and Outs of Unemployment” (Shimer, 2012), and extends the framework using the latest data during the Covid-19 pandemic.

## How to run the package
Shimer (2012) processed monthly CPS files from January 1976 to January 2005. You can download and analyze more recent data using our code. The default time span is January 1976 - March 2021. You can compile this package by typing
```
python -m src start_date=197601 end_date=202110
```
This command activates an analysis from January 1976 to October 2021. You can input any interval as long as there is raw data.

## Sources of Raw Data
There are two sources of raw CPS Basic Monthly data: [NBER.org](https://data.nber.org/cps-basic2/) and [Census.gov](https://www.census.gov/data/datasets/time-series/demo/cps/cps-basic.html). We made available 3 possible solutions that our users can choose from:
1. Download from NBER.org
2. Download from Census.gov
3. Download from a mixture of NBER.org (for files earlier than 1994) and Census.gov (for files later than 1994). 

Since [Census.gov](https://www.census.gov/data/datasets/time-series/demo/cps/cps-basic.html) does not support downloading data files older than 1994 but is more up-to-date than [NBER.org](https://data.nber.org/cps-basic2/) in terms of newly published data, we suggest using the third method.

## Environment and Prerequisite Installations
This package is built on and tested on Python 3.6.
