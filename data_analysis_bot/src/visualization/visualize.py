''''
Transforming the ../notebooks/visualization.ipynb in a python script

'''


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Average per Sector

def sector_avg(df):
    
    sector_avg = df.groupby('Setor').mean()['NPS interno'].round(2)


    plt.figure(figsize = (12,3))
    sns.barplot(sector_avg.index, sector_avg.values)

    plt.yticks(np.arange(0, 11,1))
    plt.title('NPS Interno Médio x Setor')
    plt.ylabel('NPS Interno Médio')
    plt.xlabel('Setor');

    return plt.figure()

# Average per Type of Contract

sector_avg = df.groupby('Tipo de Contratação').mean()['NPS interno'].round(2)


plt.figure(figsize = (12,3))
sns.barplot(sector_avg.index, sector_avg.values)

plt.yticks(np.arange(0, 11,1))
plt.title('NPS Interno Médio x Tipo de Contratação')
plt.ylabel('NPS Interno Médio')
plt.xlabel('Tipo de Contratação');
