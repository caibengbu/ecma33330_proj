import numpy as np
import pandas as pd

def seasonal_adjust(df):
    print("seasonal adjusting ...")
    df['flowsEE'] = df.flowEE/(df.flowEE+df.flowEI+df.flowEU)
    df['flowsEI'] = df.flowEI/(df.flowEE+df.flowEI+df.flowEU)
    df['flowsEU'] = df.flowEU/(df.flowEE+df.flowEI+df.flowEU)
    df['flowsUE'] = df.flowUE/(df.flowUE+df.flowUI+df.flowUU)
    df['flowsUU'] = df.flowUU/(df.flowUE+df.flowUI+df.flowUU)
    df['flowsUI'] = df.flowUI/(df.flowUE+df.flowUI+df.flowUU)
    df['flowsIE'] = df.flowIE/(df.flowIE+df.flowII+df.flowIU)
    df['flowsIU'] = df.flowIU/(df.flowIE+df.flowII+df.flowIU)
    df['flowsII'] = df.flowII/(df.flowIE+df.flowII+df.flowIU)

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

    data = {}
    for name in ["flowsEI","flowsEU","flowsUE","flowsUI","flowsIE","flowsIU"]:
        flowsXY = df[name]
        l6 = shift(flowsXY,6)
        l5 = shift(flowsXY,5)
        l4 = shift(flowsXY,4)
        l3 = shift(flowsXY,3)
        l2 = shift(flowsXY,2)
        l1 = shift(flowsXY,1)
        f1 = shift(flowsXY,-1)
        f2 = shift(flowsXY,-2)
        f3 = shift(flowsXY,-3)
        f4 = shift(flowsXY,-4)
        f5 = shift(flowsXY,-5)
        f6 = shift(flowsXY,-6)
        ma = (0.5*l6 + l5 + l4 + l3 + l2 + l1 + flowsXY + f1 + f2 + f3 + f4 + f5 + 0.5*f6)/12
        ratio = flowsXY/ma
        month_id = df.date.apply(lambda x: int(x[4:6]))
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
        sa_xy = flowsXY/ratio
        directions = name[5:7].lower()
        data[directions] = np.nan_to_num(sa_xy)
    return pd.DataFrame(data)



