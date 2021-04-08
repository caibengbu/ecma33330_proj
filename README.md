# Replicating Shimer (2012)

This repostory manages codes for replicating “Reassessing the Ins and Outs of Unemployment” (Shimer, 2012), and extends the framework to more recent data during the Covid-19 pandemic.

## How to run the package
Shimer (2012) processed monthly CPS files from January 1976 to January 2005. You can download and analyze with more recent data using our code. The default timespan is January 1976 - September 2020. You can compile this package by typing
```
make
```
in your Mac OS terminal. If you want to conduct analysis on a period of time with customized start date and end date, for example January 1994 - December 2010, you can type in Shell Terminal
```
make START_DATE=199401 END_DATE=201012
```
To analyze the data from January 1994 to December 2012 only.

## Environment
This package is built on and tested on Stata SE 16.1 (with terminal utility), Wolframcript and GNU Make 3.81.
