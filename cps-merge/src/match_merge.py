import pandas as pd
import sys
filename1 = "../input/cps"+sys.argv[1]+".csv"
filename2 = "../input/cps"+sys.argv[2]+".csv"
df1 = pd.read_csv(filename1,dtype="float64")
df2 = pd.read_csv(filename2,dtype="float64")
df1['hh'] = df1.hh.replace('( |-|/)','',regex=True).astype("float64")
df2['hh'] = df2.hh.replace('( |-|/)','',regex=True).astype("float64") # Filter instances like '5-6139622701' and '0 3001251506'
df1['race'] = pd.to_numeric(df1['race'],errors="coerce")
df2['race'] = pd.to_numeric(df2['race'],errors="coerce")

df1 = df1[(df1.mis != 4) & (df1.mis != 8)]
df2 = df2[(df2.mis != 1) & (df2.mis != 5)]

# gen mis0 = mis1 - 1
df1['mis0'] = df1['mis']
df2['mis0'] = df2['mis'] - 1

# flag dups
df1['is_dup'] = df1.duplicated(subset=["hh","line", "race", "sex", "age", "mis0"],keep=False)
df2['is_dup'] = df2.duplicated(subset=["hh","line", "race", "sex", "age", "mis0"],keep=False)
df1['dup'] = - df1.groupby(["hh","line", "race", "sex", "age", "mis0"]).cumcount() - df1['is_dup'] # negative flag
df2['dup'] = df2.groupby(["hh","line", "race", "sex", "age", "mis0"]).cumcount() + df2['is_dup'] # positive flag


# Merge
df_merge1 = df1.merge(df2,how='outer',on=["hh", "line", "race", "sex", "age", "mis0","dup"],indicator=True)
df_merge1 = df_merge1.rename(columns={'_merge':'_merge1'})

# Change age to age - 1 and merge again
df_touse = df_merge1[df_merge1._merge1=="right_only"].copy()
df_touse.loc[:,'age'] = df_touse.loc[:,'age']-1
df_touse = df_touse.drop(df_touse.filter(like='_x', axis=1).columns,axis=1)
df_touse = df_touse.drop('_merge1',axis=1)
df_touse.columns = df_touse.columns.str.replace(r'_y$', '')
df_master_only = df_merge1[df_merge1._merge1=="left_only"]
df_master_only = df_master_only.drop(df_master_only.filter(like='_y', axis=1).columns,axis=1)
df_master_only = df_master_only.drop('_merge1',axis=1)
df_master_only.columns = df_master_only.columns.str.replace(r'_x$', '')
df_update = df_master_only.merge(df_touse,how='outer',on=["hh", "line", "race", "sex", "age", "mis0","dup"],indicator=True)
df = pd.concat([df_merge1,df_update[df_update._merge == "both"]])

# Deal with Duplicates
df = df[~((df.duplicated(subset=["hh", "line", "race", "sex", "age", "mis0", "dup"],keep=False)) & (df._merge!="both"))].copy()
df.loc[df._merge=="both",'age'] = df.loc[df._merge=="both",'age'] + 1
df = df[~((df.duplicated(subset=["hh", "line", "race", "sex", "age", "mis0", "dup"],keep=False)) & (df._merge!="both"))]
df.loc[df._merge=="both","_merge1"] = "both"

df.to_csv('../output/merg'+sys.argv[1]+"_"+sys.argv[2]+'.csv',index=False)