# -*- coding: utf-8 -*-
"""
Created on Fri Jun  1 12:02:10 2018

@author: JITESH
"""

import pandas as pd
import numpy as np

data=pd.read_csv("stats_females.csv")

md_height=data.iloc[:,1:].values
height=data.iloc[:,0].values

from sklearn.model_selection import train_test_split
md_train,md_test,h_train,h_test=train_test_split(md_height,height,test_size=0.2,random_state=0)

from sklearn.linear_model import LinearRegression
regressor=LinearRegression()
regressor.fit(md_train,h_train)

import statsmodels.formula.api as sm
md_height=np.append(arr=np.ones((214,1)).astype(int),values=md_height,axis=1)

md_height_opt=md_height[:,[0,1,2]]
regressor_OLS=sm.OLS(endog=height,exog=md_height_opt).fit()
regressor_OLS.summary()

params=regressor_OLS.params
print params




