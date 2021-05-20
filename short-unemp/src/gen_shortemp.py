import pandas as pd
import sys
date = int(sys.argv[1])
filename = "../input/cps"+sys.argv[1]+".csv"
df = pd.read_csv(filename,dtype="float64")
df = df[(df.mis==1) | (df.mis==5)]
df = df[df.age>=16]
if date>197600 and date<198900:
    df = df[df.status==3]
else:
    df = df[(df.status==3) | (df.status==4)]

df['tag'] = df.apply(lambda x: 1 if x.dur<=4 else 0, axis=1)
tag0 = df.groupby(['tag']).agg({'fweight': 'sum'}).fweight[0]
tag1 = df.groupby(['tag']).agg({'fweight': 'sum'}).fweight[1]
short = tag1/(tag0+tag1)

out_filename = "../output/short_unemp_"+sys.argv[1]+".txt"
with open(out_filename,'w') as f:
    f.write(f"{short},{date}\n")
