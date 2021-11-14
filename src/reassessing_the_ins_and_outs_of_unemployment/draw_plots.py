import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
from datetime import datetime
from .other_utils import get_output_filename, get_figures_filename

def plot_all(start_date,end_date,theDir):
    print("generating plots ...")
    ei = np.loadtxt(get_output_filename(theDir,'eiM_rate.txt'), delimiter = "\t")
    eu = np.loadtxt(get_output_filename(theDir,'euM_rate.txt'), delimiter = "\t")
    ie = np.loadtxt(get_output_filename(theDir,'ieM_rate.txt'), delimiter = "\t")
    iu = np.loadtxt(get_output_filename(theDir,'iuM_rate.txt'), delimiter = "\t")
    ue = np.loadtxt(get_output_filename(theDir,'ueM_rate.txt'), delimiter = "\t")
    ui = np.loadtxt(get_output_filename(theDir,'uiM_rate.txt'), delimiter = "\t")
    unemp = pd.read_csv(os.path.join(theDir,'raw','LNS14000000.txt'), delim_whitespace=True, names=['date', 'unemp'])
    unemp = unemp.head(len(ei)) #Make sure the two files are of equal length
    unemp['unemp'] = unemp['unemp']/100

    main_df = pd.DataFrame(np.column_stack([ei, eu, ie, iu, ue, ui]), columns=['ei_M', 'eu_M', 'ie_M', 'iu_M', 'ue_M', 'ui_M'])
    start_date_datetime = datetime.strptime(start_date,"%Y%m")
    end_date_datetime = datetime.strptime(end_date,"%Y%m")
    
    dates = pd.date_range(start_date_datetime, end_date_datetime, freq='M')
    main_df['dates'] = dates

    main_df['sse'] = main_df['iu_M']*main_df['ue_M'] + main_df['ui_M']*main_df['ie_M'] + main_df['ue_M']*main_df['ie_M']
    main_df['ssu'] = main_df['ei_M']*main_df['iu_M'] + main_df['ie_M']*main_df['eu_M'] + main_df['iu_M']*main_df['eu_M']
    main_df['ssi'] = main_df['eu_M']*main_df['ui_M'] + main_df['ue_M']*main_df['ei_M'] + main_df['ui_M']*main_df['ei_M']

    main_df['urate'] = main_df['ssu'] / (main_df['ssu'] + main_df['sse'])
    main_df['erate'] = main_df['sse'] / (main_df['ssu'] + main_df['sse'] + main_df['ssi'])

    #Using iu, other fixed
    main_df['sse'] = main_df['iu_M']*main_df['ue_M'].mean() + main_df['ui_M'].mean()*main_df['ie_M'].mean() + main_df['ue_M'].mean()*main_df['ie_M'].mean()
    main_df['ssu'] = main_df['ei_M'].mean()*main_df['iu_M'] + main_df['ie_M'].mean()*main_df['eu_M'].mean() + main_df['iu_M']*main_df['eu_M'].mean()
    main_df['ssi'] = main_df['eu_M'].mean()*main_df['ui_M'].mean() + main_df['ue_M'].mean()*main_df['ei_M'].mean() + main_df['ui_M'].mean()*main_df['ei_M'].mean()

    main_df['urate_iu'] = main_df['ssu'] / (main_df['ssu'] + main_df['sse'])
    main_df['erate_iu'] = main_df['sse'] / (main_df['ssu'] + main_df['sse'] + main_df['ssi'])

    #Using ie, other fixed
    main_df['sse'] = main_df['iu_M'].mean()*main_df['ue_M'].mean() + main_df['ui_M'].mean()*main_df['ie_M'] + main_df['ue_M'].mean()*main_df['ie_M']
    main_df['ssu'] = main_df['ei_M'].mean()*main_df['iu_M'].mean() + main_df['ie_M']*main_df['eu_M'].mean() + main_df['iu_M'].mean()*main_df['eu_M'].mean()
    main_df['ssi'] = main_df['eu_M'].mean()*main_df['ui_M'].mean() + main_df['ue_M'].mean()*main_df['ei_M'].mean() + main_df['ui_M'].mean()*main_df['ei_M'].mean()

    main_df['urate_ie'] = main_df['ssu'] / (main_df['ssu'] + main_df['sse'])
    main_df['erate_ie'] = main_df['sse'] / (main_df['ssu'] + main_df['sse'] + main_df['ssi'])

    #Using ei, other fixed
    main_df['sse'] = main_df['iu_M'].mean()*main_df['ue_M'].mean() + main_df['ui_M'].mean()*main_df['ie_M'].mean() + main_df['ue_M'].mean()*main_df['ie_M'].mean()
    main_df['ssu'] = main_df['ei_M']*main_df['iu_M'].mean() + main_df['ie_M'].mean()*main_df['eu_M'].mean() + main_df['iu_M'].mean()*main_df['eu_M'].mean()
    main_df['ssi'] = main_df['eu_M'].mean()*main_df['ui_M'].mean() + main_df['ue_M'].mean()*main_df['ei_M'] + main_df['ui_M'].mean()*main_df['ei_M']

    main_df['urate_ei'] = main_df['ssu'] / (main_df['ssu'] + main_df['sse'])
    main_df['erate_ei'] = main_df['sse'] / (main_df['ssu'] + main_df['sse'] + main_df['ssi'])

    #Using eu, other fixed
    main_df['sse'] = main_df['iu_M'].mean()*main_df['ue_M'].mean() + main_df['ui_M'].mean()*main_df['ie_M'].mean() + main_df['ue_M'].mean()*main_df['ie_M'].mean()
    main_df['ssu'] = main_df['ei_M'].mean()*main_df['iu_M'].mean() + main_df['ie_M'].mean()*main_df['eu_M'] + main_df['iu_M'].mean()*main_df['eu_M']
    main_df['ssi'] = main_df['eu_M']*main_df['ui_M'].mean() + main_df['ue_M'].mean()*main_df['ei_M'].mean() + main_df['ui_M'].mean()*main_df['ei_M'].mean()

    main_df['urate_eu'] = main_df['ssu'] / (main_df['ssu'] + main_df['sse'])
    main_df['erate_eu'] = main_df['sse'] / (main_df['ssu'] + main_df['sse'] + main_df['ssi'])

    #Using ue, other fixed
    main_df['sse'] = main_df['iu_M'].mean()*main_df['ue_M'] + main_df['ui_M'].mean()*main_df['ie_M'].mean() + main_df['ue_M']*main_df['ie_M'].mean()
    main_df['ssu'] = main_df['ei_M'].mean()*main_df['iu_M'].mean() + main_df['ie_M'].mean()*main_df['eu_M'].mean() + main_df['iu_M'].mean()*main_df['eu_M'].mean()
    main_df['ssi'] = main_df['eu_M'].mean()*main_df['ui_M'].mean() + main_df['ue_M']*main_df['ei_M'].mean() + main_df['ui_M'].mean()*main_df['ei_M'].mean()

    main_df['urate_ue'] = main_df['ssu'] / (main_df['ssu'] + main_df['sse'])
    main_df['erate_ue'] = main_df['sse'] / (main_df['ssu'] + main_df['sse'] + main_df['ssi'])

    #Using ui, other fixed
    main_df['sse'] = main_df['iu_M'].mean()*main_df['ue_M'].mean() + main_df['ui_M']*main_df['ie_M'].mean() + main_df['ue_M'].mean()*main_df['ie_M'].mean()
    main_df['ssu'] = main_df['ei_M'].mean()*main_df['iu_M'].mean() + main_df['ie_M'].mean()*main_df['eu_M'].mean() + main_df['iu_M'].mean()*main_df['eu_M'].mean()
    main_df['ssi'] = main_df['eu_M'].mean()*main_df['ui_M'] + main_df['ue_M'].mean()*main_df['ei_M'].mean() + main_df['ui_M']*main_df['ei_M'].mean()

    main_df['urate_ui'] = main_df['ssu'] / (main_df['ssu'] + main_df['sse'])
    main_df['erate_ui'] = main_df['sse'] / (main_df['ssu'] + main_df['sse'] + main_df['ssi'])
    
    for varname in ['urate_ei', 'urate_eu', 'urate_ui' , 'urate_ue', 'urate_iu', 'urate_ie']:
        main_df[['dates', varname]].to_csv(get_output_filename(theDir,varname+'.dat'))
        plt.plot(main_df['dates'], main_df[varname], label='Hypothetical from '+varname)
        plt.plot(main_df['dates'], unemp['unemp'], label='Actual unemployment rate')
        plt.legend()
        plt.savefig(get_figures_filename(theDir,'fig5'+varname+'.png'))
        plt.close()