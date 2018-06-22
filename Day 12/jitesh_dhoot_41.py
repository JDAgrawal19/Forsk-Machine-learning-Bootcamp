# -*- coding: utf-8 -*-
"""
Created on Fri May 25 12:55:57 2018

@author: JITESH
"""

import pandas as pd
import numpy as np


df=pd.read_csv("Automobile.csv")

df['price']=df['price'].fillna(df['price'].mean())

price = df["price"].values

max(price)

min(price)

print np.mean(price)

print np.std(price)




