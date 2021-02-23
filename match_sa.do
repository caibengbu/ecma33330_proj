local baseyear 2003 /* baseyear was 1998 in Shimer's original code */
use flows, clear
drop if date==.
gen flowsEE = flowEE/(flowEE+flowEI+flowEU)
gen flowsEI = flowEI/(flowEE+flowEI+flowEU)
gen flowsEU = flowEU/(flowEE+flowEI+flowEU)
gen flowsUE = flowUE/(flowUE+flowUI+flowUU)
gen flowsUU = flowUU/(flowUE+flowUI+flowUU)
gen flowsUI = flowUI/(flowUE+flowUI+flowUU)
gen flowsIE = flowIE/(flowIE+flowII+flowIU)
gen flowsIU = flowIU/(flowIE+flowII+flowIU)
gen flowsII = flowII/(flowIE+flowII+flowIU)
drop flowE* flowU* flowI* flowM*
aorder

sort date
gen int time = _n
gen int year = int( date /100 )
gen int month = int( (date - year*100) )
gen t = year + (month-1) / 12
tsset time

*** Seasonally adjust the flows (ratio-to-MA method):
local Y1 = "E"
local Y2 = "U"
local Y3 = "I"

qui foreach XY in EE EU EI UE UU UI IE IU II {
	local `XY' EE
    gen MA_`XY' = .5*L6.flows`XY' + L5.flows`XY' + L4.flows`XY' + L3.flows`XY' + L2.flows`XY' + L.flows`XY' + flows`XY' + F.flows`XY' + F2.flows`XY' + F3.flows`XY' + F4.flows`XY' + F5.flows`XY' + .5*F6.flows`XY'
    replace MA_`XY' = MA_`XY' / 12
    gen ratio = flows`XY' / MA_`XY'
    for M in num 1 2 to 12: egen ratioM = mean(ratio) if month==M
    for M in num 1 2 to 12: replace ratio = ratioM if month==M
    means ratio if year==`baseyear'
    local k = r(mean_g)
    replace ratio = ratio / `k'
    gen SA_`XY' = flows`XY' / ratio
    replace SA_`XY' = 0 if SA_`XY'==. & flowsEE~=.
    drop ratio*
    sort time
}

keep date SA_*

save seasadj.dta, replace

*** Export the seasonally adjusted data to a text file.
outfile SA_EU using eu.txt, replace
outfile SA_EI using ei.txt, replace
outfile SA_UE using ue.txt, replace
outfile SA_UI using ui.txt, replace
outfile SA_IE using ie.txt, replace
outfile SA_IU using iu.txt, replace
