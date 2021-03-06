# Replicating Shimer (2012)

This repository manages codes for replicating “Reassessing the Ins and Outs of Unemployment” (Shimer, 2012), and extends the framework using the latest data during the Covid-19 pandemic.

## How to run the package
Shimer (2012) processed monthly CPS files from January 1976 to January 2005. You can download and analyze more recent data using our code. The default time span is January 1976 - March 2021. You can compile this package by typing
```
make
```
in your terminal. If you want to analyze a period with a customized time span, for example, January 1994 - December 2010, you can type in your terminal
```
make START_DATE=199401 END_DATE=201012
```
This command activates an analysis from January 1994 to December 2012 only.

## Sources of Raw Data
There are two sources of raw CPS Basic Monthly data: [NBER.org](https://data.nber.org/cps-basic2/) and [Census.gov](https://www.census.gov/data/datasets/time-series/demo/cps/cps-basic.html). We made available 3 possible solutions that our users can choose from:
1. Download from NBER.org
2. Download from Census.gov
3. Download from a mixture of NBER.org (for files earlier than 1994) and Census.gov (for files later than 1994). 

Since [Census.gov](https://www.census.gov/data/datasets/time-series/demo/cps/cps-basic.html) does not support downloading data files older than 1994 but is more up-to-date than [NBER.org](https://data.nber.org/cps-basic2/) in terms of newly published data, we suggest using the third method.

## Environment and Prerequisite Installations
This package is built on and tested on Python 3.6 and GNU Make 3.81. Depending on your OS version, you might or might not have `wget` installed. We primarily use `wget` to fetch data from data sources. You can install `wget` by typing `brew install wget` in your terminal.
