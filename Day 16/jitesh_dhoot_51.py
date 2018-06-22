# -*- coding: utf-8 -*-
"""
Created on Thu May 31 11:13:08 2018

@author: JITESH
"""

import pandas as pd


data=pd.read_csv("Bahubali2_vs_Dangal.csv")

day=data.iloc[:,0].values
bahubali=data.iloc[:,1].values
dangal=data.iloc[:,2].values
bahubali=bahubali.reshape(-1,1)
dangal=dangal.reshape(-1,1)
day=day.reshape(-1,1)


from sklearn.linear_model import LinearRegression
bahu_model=LinearRegression()
dangal_model=LinearRegression()


bahu_model.fit(day,bahubali)

dangal_model.fit(day,dangal)


bahu_day_10=bahu_model.predict(10)
dangal_day_10=dangal_model.predict(10)


