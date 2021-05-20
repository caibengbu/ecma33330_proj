from scipy import optimize, sparse as sp
from scipy.sparse.linalg import inv
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from scipy import optimize as opt


def logTrend(vec,smooth):
    T = len(vec)
    line_1 = sp.csr_matrix((np.array([-1.,2.,-1.]),(np.zeros(3),np.arange(3))),shape=(1,T))
    line_2 = sp.csr_matrix((np.array([2.,-5.,4.,-1.]),(np.zeros(4),np.arange(4))),shape=(1,T))
    body = sp.diags([-1.,4.,-6.,4.,-1.],range(5),shape=(T-4,T))
    line_end2 = sp.csr_matrix((np.array([-1.,4.,-5.,2.]),(np.zeros(4),np.arange(T-4,T))),shape=(1,T))
    line_end1 = sp.csr_matrix((np.array([-1.,2.,-1.]),(np.zeros(3),np.arange(T-3,T))),shape=(1,T))
    A = sp.vstack((line_1,line_2,body,line_end2,line_end1))
    B = inv(sp.identity(T).tocsc() - smooth*A.tocsc())
    return B.dot(np.log(vec))
    
def Detrend(vec,smooth):
    return np.log(vec) - logTrend(vec,smooth)

def read_withDate(filename,delimiter,skiprows=0):
    temp = pd.read_csv(filename,header=None,delimiter=delimiter,skiprows=skiprows,names=["date","data"])
    date = temp.date.values
    date_pandas = pd.to_datetime(date,format='%Y%m')
    return temp.set_index(date_pandas).data

smooth = 10**5
UnempM = read_withDate("../output/unemp.txt",delimiter=" ")
EmpM = read_withDate("../output/emp.txt",delimiter=" ")
ShortM = read_withDate("../output/short_emp.txt",delimiter=" ")
ShortShareM = read_withDate("short-unemp-x13.d11",delimiter="\t",skiprows=2)
ShortAdjM = ShortShareM * UnempM

plt.plot(ShortAdjM,label="from CPS")
plt.plot(ShortM,label="from BLS")
plt.legend(loc=0)
plt.savefig("../output/adjusted_short_unemp.png")

FindM = 1 - (UnempM-ShortAdjM)/UnempM
findM = -np.log(1-FindM)
UrateM = UnempM/(UnempM+EmpM)

# Construct Separation Rate
def eq5(x_t,u_tp1,u_t,f_t,l_t):
    return u_tp1-np.exp(-f_t-x_t)*u_t-(1-np.exp(-f_t-x_t))*x_t*l_t/(f_t+x_t)

sepM = []
for t in range(len(UnempM)-1):
    u_tp1 = UnempM[t+1]
    u_t = UnempM[t]
    f_t = findM[t]
    l_t = UnempM[t]+EmpM[t]
    f = lambda x: eq5(x,u_tp1,u_t,f_t,l_t)
    sol = opt.root_scalar(f, bracket=[0, 1], method='brentq')
    sepM.append(sol.root)

sepM = pd.Series(sepM,index=UnempM.index[0:-1]).copy()
SepM = 1-np.exp(-sepM)

findQ = findM.resample('Q').mean()
UrateQ = UrateM.resample('Q').mean()
sepQ = sepM.resample('Q').mean()
UrateQ = UrateM.resample('Q').mean()
uss = sepQ/(sepQ+findQ)
uf = np.mean(sepQ)/(np.mean(sepQ)+findQ)
us = sepQ/(sepQ+np.mean(findQ))