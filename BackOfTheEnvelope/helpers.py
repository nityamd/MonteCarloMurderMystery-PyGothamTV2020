import pandas as pd
import numpy as np

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
