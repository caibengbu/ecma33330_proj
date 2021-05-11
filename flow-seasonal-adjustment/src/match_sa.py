import numpy as np

date,flowEE,flowEI,flowEU,flowEM,flowUE,flowUI,flowUU,flowUM,flowIE,flowII,flowIU,flowIM,flowME,flowMI,flowMU = np.genfromtxt("../input/flows.txt",delimiter=",",unpack=True)
flowsEE = flowEE/(flowEE+flowEI+flowEU)
flowsEI = flowEI/(flowEE+flowEI+flowEU)
flowsEU = flowEU/(flowEE+flowEI+flowEU)
flowsUE = flowUE/(flowUE+flowUI+flowUU)
flowsUU = flowUU/(flowUE+flowUI+flowUU)
flowsUI = flowUI/(flowUE+flowUI+flowUU)
flowsIE = flowIE/(flowIE+flowII+flowIU)
flowsIU = flowIU/(flowIE+flowII+flowIU)
flowsII = flowII/(flowIE+flowII+flowIU)

def shift(vec,shift_num):
    vec_temp = np.roll(vec,shift_num)
    if shift_num>0:
        vec_temp[:shift_num] = np.NaN
    else:
        vec_temp[shift_num:] = np.NaN
    return vec_temp

def gmean(np_vec):
    non_nan_lenth = sum(~np.isnan(np_vec))
    cumprod = np.nanprod(np_vec)
    return cumprod**(1/non_nan_lenth)

for name in ["flowsEI","flowsEU","flowsUE","flowsUI","flowsIE","flowsIU"]:
    flowsXY = eval(name)
    L6 = shift(flowsXY,6)
    L5 = shift(flowsXY,5)
    L4 = shift(flowsXY,4)
    L3 = shift(flowsXY,3)
    L2 = shift(flowsXY,2)
    L1 = shift(flowsXY,1)
    F1 = shift(flowsXY,-1)
    F2 = shift(flowsXY,-2)
    F3 = shift(flowsXY,-3)
    F4 = shift(flowsXY,-4)
    F5 = shift(flowsXY,-5)
    F6 = shift(flowsXY,-6)
    MA = (0.5*L6 + L5 + L4 + L3 + L2 + L1 + flowsXY + F1 + F2 + F3 + F4 + F5 + 0.5*F6)/12
    ratio = flowsXY/MA
    month_id = date % 100
    ratio_jan = np.nanmean(ratio[month_id==1])
    ratio_feb = np.nanmean(ratio[month_id==2])
    ratio_mar = np.nanmean(ratio[month_id==3])
    ratio_apr = np.nanmean(ratio[month_id==4])
    ratio_may = np.nanmean(ratio[month_id==5])
    ratio_jun = np.nanmean(ratio[month_id==6])
    ratio_jul = np.nanmean(ratio[month_id==7])
    ratio_aug = np.nanmean(ratio[month_id==8])
    ratio_sep = np.nanmean(ratio[month_id==9])
    ratio_oct = np.nanmean(ratio[month_id==10])
    ratio_nov = np.nanmean(ratio[month_id==11])
    ratio_dec = np.nanmean(ratio[month_id==12])
    ratio[month_id==1] = ratio_jan
    ratio[month_id==2] = ratio_feb
    ratio[month_id==3] = ratio_mar
    ratio[month_id==4] = ratio_apr
    ratio[month_id==5] = ratio_may
    ratio[month_id==6] = ratio_jun
    ratio[month_id==7] = ratio_jul
    ratio[month_id==8] = ratio_aug
    ratio[month_id==9] = ratio_sep
    ratio[month_id==10] = ratio_oct
    ratio[month_id==11] = ratio_nov
    ratio[month_id==12] = ratio_dec
    gmean_ratio = gmean(np.array([ratio_jan,ratio_feb,ratio_mar,ratio_apr,ratio_may,ratio_jun,ratio_jul,ratio_aug,ratio_sep,ratio_oct,ratio_nov,ratio_dec]))
    ratio = ratio/gmean_ratio
    SA_XY = flowsXY/ratio
    directions = name[5:7].lower()
    np.savetxt(f"../output/{directions}.txt",np.nan_to_num(SA_XY))



