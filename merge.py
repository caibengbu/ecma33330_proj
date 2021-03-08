import os

dataDir = "cpsbasic_data/"
assert os.path.exists(theDir)

list_of_datafile = [f for f in os.listdir(path=dataDir) if f[0].isdigit() and (f.endswith(".cps") or f.endswith(".dat"))]
list_of_datafile.sort()

# match_extract.do
for datafile in list_of_datafile:
    arg = os.path.splitext(datafile)[0]
    print("Running match_extract.do via STATA, arg = " + arg)
    os.system("bash -c 'cat " + dataDir + datafile + " > " + arg + ".raw'")
    os.system("bash -c 'stata-se -e match_extract.do " + arg + "'")
    os.remove(arg + ".raw")

# match_merge.do
for i in range(len(list_of_datafile)):
    if i!=0:
        arg1 = os.path.splitext(list_of_datafile[i-1])[0]
        arg2 = os.path.splitext(list_of_datafile[i])[0]
        if arg2 in ['199506','199507','199508','199509']:
            continue
        else:
            print("Running match_merge.do via STATA, args = [" + arg1 + ", " + arg2 + "]")
            os.system("bash -c 'stata-se -e match_merge.do " + arg1 + " " + arg2 + "'")
            

# create_flows.do
print("Running create_flows.do via STATA")
os.system("bash -c 'stata-se -e create_flows.do'")

# match_flows.do
for i in range(len(list_of_datafile)):
    if i!=0:
        arg = os.path.splitext(list_of_datafile[i])[0]
        if arg in ['199506','199507','199508','199509']:
            print("Running empty_flow.do via STATA, arg = " + arg)
            os.system("bash -c 'stata-se -e empty_flow.do " + arg + "'")
        else:
            print("Running match_flow.do via STATA, arg = " + arg)
            os.system("bash -c 'stata-se -e match_flow.do " + arg + "'")

# match_sa.do
print("Running match_sa.do via STATA")
os.system("bash -c 'stata-se -e match_sa.do'")
    
# three-state.nb -> three-state.wls
print("Computing lambdas")
os.system("bash -c './three-state.wls'")

# Clean intermediate files
os.system("bash -c 'rm cps*.dta merg*.dta'")
