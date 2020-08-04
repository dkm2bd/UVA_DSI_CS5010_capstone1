# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 20:04:25 2020

@author: darak
"""
import pandas as pd

# Write function to clean data
def cleanNumeric(df, exclude):
    
    df2 = df.copy()
    
    for col in df2.columns:
        df2[col] = df2[col].astype(str)  # cast to string
        df2[col] = df2[col].str.replace(',', '').str.replace('%','').str.replace('+','')

        if col not in exclude:
            df2[col] = df2[col].astype(float)  # cast to float
            
    return df2


def divideDf (df, col1, col2):
    
    df2 = df.copy()
    
    colNew = col1 + '%'
    df2[colNew] = df2[col1]/df2[col2] * 100
    
    return df2
