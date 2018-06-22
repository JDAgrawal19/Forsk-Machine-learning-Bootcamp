# -*- coding: utf-8 -*-
"""
Created on Mon May 28 12:37:15 2018

@author: JITESH
"""

import pandas as pd

dataset=pd.read_csv("Cars.csv")
features=dataset.iloc[:,1:].values
price=dataset.iloc[:,0].values


from sklearn.model_selection import train_test_split

features_train,features_test,price_train,price_test=train_test_split(features,price,test_size=0.5,random_state=0)

features_train_df = pd.DataFrame(features_train)

features_test_df = pd.DataFrame(features_test)
price_train_df = pd.DataFrame(price_train)
price_test_df = pd.DataFrame(price_test)

features_train_df.to_csv("f_train.csv",sep=',',encoding='utf-8')

features_test_df.to_csv("f_test.csv",sep=',',encoding='utf-8')

price_train_df.to_csv("p_train.csv",sep=',',encoding='utf-8')

price_test_df.to_csv("p_test.csv",sep=',',encoding='utf-8')
