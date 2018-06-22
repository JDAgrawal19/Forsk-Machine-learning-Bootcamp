# -*- coding: utf-8 -*-
"""
Created on Fri Jun  1 11:14:45 2018

@author: JITESH
"""

import pandas as pd

data=pd.read_csv("iq_size.csv")

feature=data.iloc[:,1:].values
piq=data.iloc[:,0].values

from sklearn.model_selection import train_test_split
f_train,f_test,iq_train,iq_test=train_test_split(feature,piq,test_size=0.2,random_state=0)

from sklearn.linear_model import LinearRegression
regressor=LinearRegression()
regressor.fit(f_train,iq_train)

a=[90,70,150]
import numpy as np
a=np.array(a).reshape(1,-1)

regressor.predict(a)

import statsmodels.formula.api as sm
feature=np.append(arr=np.ones((38,1)).astype(int),values=feature,axis=1)

features_opt=feature[:,[0,1,2,3]]
regressor_OLS=sm.OLS(endog=piq,exog=features_opt).fit()
regressor_OLS.summary()

features_opt=feature[:,[0,1,2]]
regressor_OLS=sm.OLS(endog=piq,exog=features_opt).fit()
regressor_OLS.summary()

print "weight is not a neccessary parameter"