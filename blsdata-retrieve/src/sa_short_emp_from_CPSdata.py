import pandas as pd

unadjusted_short_unemp_for_CPS = pd.read_csv("../input/short_unemp_ts.txt",delimiter=",",header=None)
unadjusted_short_unemp_for_CPS.columns = ["unemp","date"]

unemp = unadjusted_short_unemp_for_CPS.unemp.values.tolist()
date = unadjusted_short_unemp_for_CPS.date.values.tolist()
year = [aDate // 100 for aDate in date]
month = [aDate % 100 for aDate in date]

a = ""
for i in range(len(unemp)):
    a = a + str(date[i] // 100) + " " + str(date[i] % 100) + " " + str(unemp[i]) + "\n"

with open('data.dat','w') as f:
    f.write(a)


spec_text = """
series{
    file = "data.dat"
    period = 12
    format = Datevalue
}
transform{
    function = auto
}
regression{
    variables = ()
    aictest = ( td easter )
    savelog = aictest
}
outlier{
    types = ( AO LS )
}
automdl{
    savelog = amd
}
forecast{
    maxlead = 12
    print = none
}
x11{
    save = seasadj
}
"""

with open('short-unemp-x13.spc','w') as f:
    f.write(spec_text)