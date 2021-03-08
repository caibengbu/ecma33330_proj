use cps`1', clear
keep if mis == 1 | mis == 5
keep if age>=16
keep if status == 3 | status == 4

destring dur, replace
gen tag = 1 if dur <= 4
replace tag = 0 if tag ==.
collapse (sum) fweight, by(tag)
gen short = fweight[2] / (fweight[1]+fweight[2])
keep short
duplicates drop
gen date = `1'

append using short_ts
save short_ts, replace

