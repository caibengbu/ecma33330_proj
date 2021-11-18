# Replicating Shimer (2012)

This repository manages codes for replicating “Reassessing the Ins and Outs of Unemployment” (Shimer, 2012), and extends the framework using the latest data during the Covid-19 pandemic.

## How to run the package
First, install the package by pip
```
pip install git+https://github.com/caibengbu/ecma33330_proj.git
```
After it is installed, simply run
```
python -m reassessing_the_ins_and_outs_of_unemployment --start=197601 --end=202110
```
This command activates an analysis from January 1976 to October 2021. You can input any interval as long as there is raw data.

You can specify working directory by passing the `--dir` argument
```
python -m reassessing_the_ins_and_outs_of_unemployment --start=197601 --end=202110 --dir=path/to/wd
```
You can also specify directory with downloaded raw data by passing the `--dir_raw` argument
```
python -m reassessing_the_ins_and_outs_of_unemployment --start=197601 --end=202110 --dir_raw=path/to/raw
```
This automatically set the working directory to the parent directory of `path/to/raw`.
## Sources of Raw Data
There are two sources of raw CPS Basic Monthly data: [NBER.org](https://data.nber.org/cps-basic2/) and [Census.gov](https://www.census.gov/data/datasets/time-series/demo/cps/cps-basic.html). Since [Census.gov](https://www.census.gov/data/datasets/time-series/demo/cps/cps-basic.html) does not support downloading data files older than 1994 but is more up-to-date than [NBER.org](https://data.nber.org/cps-basic2/) in terms of newly published data, we download CPS Basic data older than 1994 from NBER and newer ones from Census.

## Environment and Prerequisite Installations
This package is built on and tested on Python 3.6. It is OS independent, tested on MacOS 10.15.7 and Windows 10. 

## Outputs
If executed without error, there would be an `output/` folder and a `figure/` folder. `output/` contains the monthly transitional probability and transitional rate between employment status. `figure/` contains the plot in which hypothetical unemployment rate and actual unemployment rate is plotted together for comparison.
