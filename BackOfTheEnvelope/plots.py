import pandas as pd
import matplotlib.pyplot as plt
import seasborn as sns

def coefplot(df):
    sns.set_context("paper", font_scale= 2)
    fig, ax = plt.subplots(figsize=(10,8))
    ax = sns.pointplot(x="mean_alpha", y="suspects", data=df, join=False, color = 'k')
    ax.set(xlabel='Culpability', ylabel='')
    i = 0
    for row, pair in enumerate(zip(df['alpha_hpd3'], df['alpha_hpd97'])):
        ax.plot(pair, [row,row],color = sns.color_palette("hls",10)[i], lw=3)
        i +=1
    plt.show()

    return
