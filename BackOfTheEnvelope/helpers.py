import pandas as pd
import numpy as np
import pymc3 as pm

def transform_df(df):
    newdf = pd.melt(df, id_vars=['suspects'], value_vars=['alibi',
                                                          'archery',
                                                          'inheritance',
                                                          'suspicion',
                                                          'animosity'])
    newdf = newdf.rename(columns={'variable': 'murder_proxy'})
    suspect_dict = dict(zip(df['suspects'].values, [0,1,2,3,4,5,6,7,8,9]))
    proxy_dict = dict(zip(['alibi', 'archery', 'inheritance', 'suspicion', 'animosity'], [0,1,2,3,4]))
    newdf['suspects'] = newdf['suspects'].apply(lambda x: suspect_dict[x])
    newdf['murder_proxy'] = newdf['murder_proxy'].apply(lambda x: proxy_dict[x])
    newdf = newdf.sort_values(by = ['suspects', 'murder_proxy'])
    return newdf

def get_results(trace):
    suspect_names = ['Viscountess Bae Zhun',  'Major Viktor Ljutenitsa', 'Ms Ingrid Hepburn',
                 'Lord Bryce Bloomington', 'Barrister Shannon Von Twist', 'Nurse Eliza Dill',
                 'Lady Barbara Bloomington', 'Mr. Miles Murdoch', 'Mr. Stan Hamilton','Python']
    summarystats = pm.summary(trace)
    alpha_mean = [summarystats.loc['alpha['+ str(x)+ ']']['mean'] for x in range(0,10)]
    alpha_hpd3 = [summarystats.loc['alpha['+ str(x)+ ']']['hpd_3%'] for x in range(0,10)]
    alpha_hpd97 = [summarystats.loc['alpha['+ str(x)+ ']']['hpd_97%'] for x in range(0,10)]
    results_df = pd.DataFrame({'suspects': suspect_names, 'mean_alpha': alpha_mean,
                               'alpha_hpd3':alpha_hpd3, 'alpha_hpd97':alpha_hpd97})
    return results_df
