clear
set obs 1
gen date = `1'
gen flowEE = .
gen flowEI = .
gen flowEU = .
gen flowEM = .
gen flowUE = .
gen flowUU = .
gen flowUI = .
gen flowUM = .
gen flowIE = .
gen flowIU = .
gen flowII = .
gen flowIM = .
gen flowME = .
gen flowMU = .
gen flowMI = .
append using flows
save flows, replace