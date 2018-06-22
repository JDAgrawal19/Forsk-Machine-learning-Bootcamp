# -*- coding: utf-8 -*-
"""
Created on Tue May 29 12:10:52 2018

@author: JITESH
"""

import pandas as pd
data=pd.read_csv("Loan.csv")
data  = data.drop("Loan_ID",axis=1)
features=data.iloc[:,:-1]
label=pd.DataFrame(data.iloc[:,-1])

for i in data.columns:
    if data[i].dtype == object:
        data[i] = data[i].astype('category')
        data[i] = data[i].cat.codes

data = pd.get_dummies(data,columns=["Property_Area"])



