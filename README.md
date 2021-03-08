# Term Project for ECMA33330: Replicating Shimer (2012)

This is the term project for ECMA33330 (Introduction to Dynamic Modeling) @ UChicago. We are aiming to replicate and extend the result of the paper "Reassessing the ins and outs of unemployment" (Shimer, 2012).

## How to run the package
Right now we only focus on a on a much smaller time span than the original paper. Contrary to Shimer (2012) who processed monthly CPS files from January 1976 to January 2005. Our replication focus on the period from January 1994 to December 2019. 
```
python downloads.py 199401 201912
python merge.py
```

## Environment
This package is built on and tested on Python 3.6, Stata SE 16.1 and Wolframcript. You also need to install stata-se terminal utility.
