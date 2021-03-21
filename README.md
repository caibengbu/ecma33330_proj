# Replicating Shimer (2012)

This repostory manages codes for replicating “Reassessing the Ins and Outs of Unemployment” (Shimer, 2012), and extends the framework to more recent data during the Covid-19 pandemic.

## How to run the package
Right now we only focus on a on a much smaller time span than the original paper. Contrary to Shimer (2012) who processed monthly CPS files from January 1976 to January 2005. Our replication focus on the period from January 1976 to December 2019. 
```
make
```
If you want to conduct analysis on a period of time with customized start date and end date. For example, you can type in Shell Terminal
```
make START_DATE=199401 END_DATE=201012
```
To analyze the data from January 1994 to December 2012 only.

## Environment
This package is built on and tested on Python 3.6, Stata SE 16.1 and Wolframcript. You also need to install stata-se terminal utility.
