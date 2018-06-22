# -*- coding: utf-8 -*-
"""
Created on Tue Jun  5 11:59:12 2018

@author: JITESH
"""
import numpy as np
import pandas as pd
data=pd.read_csv("Auto_mpg.txt",delim_whitespace=True,names=["mpg", "cylinders", "displacement","horsepower","weight","acceleration", "model year", "origin", "car name" ])

for i in data.columns:
    if data[i].dtype==object:
        print i

#data['horsepower'].replace('?',data['horsepower'].mode())
data['horsepower'][data['horsepower']=='?']=data['horsepower'].mode()[0]
data['horsepower']=data['horsepower'].astype(float)

for i in data.columns:
    print i,data[i].dtype



a=np.argmax(data['mpg'])
print data.iloc[a,0:].values

feature=data.iloc[:,1:8].values
label=data.iloc[:,0].values

from sklearn.model_selection import train_test_split
f_train,f_test,l_train,l_test=train_test_split(feature,label,test_size=0.2,random_state=0)

from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
f_train=sc.fit_transform(f_train)
f_test=sc.transform(f_test)



from sklearn.tree import DecisionTreeRegressor
regressor=DecisionTreeRegressor(random_state=0)
regressor.fit(f_train,l_train)

predict_label_tree=regressor.predict(f_test)
tree_score= regressor.score(f_test,l_test)

regressor.predict((np.asarray([6,215,215,2630,22.2,80,3])).reshape(1,-1))


from sklearn.ensemble import RandomForestRegressor
forest_regressor=RandomForestRegressor(n_estimators=10,random_state=0)
forest_regressor.fit(f_train,l_train)

forest_regressor.predict((np.asarray([6,215,215,2630,22.2,80,3])).reshape(1,-1))

predict_label_forest=forest_regressor.predict(f_test)
forest_score=forest_regressor.score(f_test,l_test)