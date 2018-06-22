# -*- coding: utf-8 -*-
"""
Created on Tue Jun  5 11:14:23 2018

@author: JITESH
"""
import numpy as np

import pandas as pd
data=pd.read_csv("PastHires.csv")

feature=data.iloc[:,0:6].values
label=data.iloc[:,6].values

from sklearn.preprocessing import LabelEncoder
label_encoder=LabelEncoder()
        
list1=[1,3,4,5]

for i in range(len(list1)):
    feature[:,list1[i]]=label_encoder.fit_transform(feature[:,list1[i]])        

label=label_encoder.fit_transform(label)

from sklearn.model_selection import train_test_split
f_train,f_test,l_train,l_test=train_test_split(feature,label,test_size=0.2,random_state=0)


from sklearn.tree import DecisionTreeRegressor
regressor=DecisionTreeRegressor(random_state=0)
regressor.fit(f_train,l_train)

regressor.score(f_test,l_test)

regressor.predict((np.asarray([10,1,4,0,1,0])).reshape(1,-1))

regressor.predict((np.asarray([10,0,4,1,0,1])).reshape(1,-1))


from sklearn.ensemble import RandomForestRegressor
forest_regressor=RandomForestRegressor(n_estimators=10,random_state=0)
forest_regressor.fit(f_train,l_train)


forest_regressor.predict((np.asarray([10,1,4,0,1,0])).reshape(1,-1))

forest_regressor.predict((np.asarray([10,0,4,1,0,1])).reshape(1,-1))

forest_regressor.score(f_test,l_test)