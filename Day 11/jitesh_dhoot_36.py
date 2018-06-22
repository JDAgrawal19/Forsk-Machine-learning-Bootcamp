# -*- coding: utf-8 -*-
"""
Created on Thu May 24 12:42:25 2018

@author: JITESH
"""

import pandas as pd

df=pd.read_csv("training_titanic.csv")

df["Child"]=0

for i in range(0,891):
    if df["Age"][i]<18:
        df["Child"][i]=1
        

print(df["Child"].value_counts())

print(df["Child"].value_counts(normalize=True))
