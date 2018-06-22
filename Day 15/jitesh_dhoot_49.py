# -*- coding: utf-8 -*-
"""
Created on Wed May 30 11:33:42 2018

@author: JITESH
"""

import pandas as pd
data=pd.read_csv("Red_Wine.csv")


for i in data.columns:
    data[i]=data[i].fillna(data[i].mode()[0])

features=data.iloc[:,:-1].values
quality=data.iloc[:,-1].values



from sklearn.preprocessing import LabelEncoder,OneHotEncoder
label_encoder=LabelEncoder()
features[:,0]=label_encoder.fit_transform(features[:,0])

onhot_encoder=OneHotEncoder(categorical_features=[0])
features=onhot_encoder.fit_transform(features).toarray()


f_df=pd.DataFrame(features)

from sklearn.model_selection import train_test_split as tts
f_train,f_test,q_train,q_test=tts(features,quality,test_size=0.2,random_state=0)


from sklearn.preprocessing import StandardScaler
sc=StandardScaler()

f1_train=sc.fit_transform(f_train)
f1_test=sc.transform(f_test)

from sklearn.preprocessing import MinMaxScaler
mmc=MinMaxScaler()

f2_train=mmc.fit_transform(f_train)
f2_test=mmc.transform(f_test)


