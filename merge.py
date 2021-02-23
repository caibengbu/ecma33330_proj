import os

list_of_datafile = [f for f in os.listdir() if f.endswith(".cps")]
list_of_datafile.sort()

# match_extract.do
for datafile in list_of_datafile:
    arg = os.path.splitext(datafile)[0]
    print("Running match_extract.do via STATA, arg = " + arg)
    os.system("bash -c 'stata-se -e match_extract.do " + arg + "'")

# match_merge.do
for i in range(len(list_of_datafile)):
    if i!=0:
        arg1 = os.path.splitext(list_of_datafile[i-1])[0]
        arg2 = os.path.splitext(list_of_datafile[i])[0]
        print("Running match_merge.do via STATA, args = [" + arg1 + ", " + arg2 + "]")
        os.system("bash -c 'stata-se -e match_merge.do " + arg1 + " " + arg2 + "'")

# create_flows.do
print("Running create_flows.do via STATA")
os.system("bash -c 'stata-se -e create_flows.do'")

# match_flows.do
list_of_mergfile = [f for f in os.listdir() if f.startswith("merg") and f.endswith(".dta")]
list_of_mergfile.sort()
for mergfile in list_of_mergfile:
    arg = os.path.splitext(mergfile)[0][4:10]
    print("Running match_flow.do via STATA, arg = " + arg)
    os.system("bash -c 'stata-se -e match_flow.do " + arg + "'")

# match_sa.do
print("Running match_sa.do via STATA")
os.system("bash -c 'stata-se -e match_sa.do'")
    
# three-state.nb -> three-state.m
os.system("bash -c 'math -run -noprompt < three-state.m'")