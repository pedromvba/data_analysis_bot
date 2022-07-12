''' In the ../notebooks/visualization.ipynb we used a .csv to import the data. however we imported it with the parameter (decimal= ',') to correct the numbers as text and decimals marked with , and not .
This won't work on the data imported by the gdrvebot from the google drive. So to solve this problem we will:
'''

import pandas as pd
import numpy as np

def transform_data(df):
    df['NPS Interno'] =  df['NPS Interno'].str.replace(',' , '.').astype('float')
    df['Setor'].replace( 'Engenheiro de Software', 'Engenharia de Software', inplace=True)
    return df
