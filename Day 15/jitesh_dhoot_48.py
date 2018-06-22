# -*- coding: utf-8 -*-
"""
Created on Wed May 30 11:03:30 2018

@author: JITESH
"""

import pandas as pd

data=pd.read_csv( 'https://raw.githubusercontent.com/rasbt/pattern_classification/master/data/wine_data.csv',
     header=None,
     usecols=[0,1,2])



data.columns=['Class label','Alcohol','Malic acid']

features=data.iloc[:,1:].values
label=data.iloc[:,0].values

from sklearn.model_selection import train_test_split as tts
f_train,f_test,l_train,l_test=tts(features,label,test_size=0.2,random_state=0)

from sklearn.preprocessing import StandardScaler
sc=StandardScaler()

f1_train=sc.fit_transform(f_train)
f1_test=sc.transform(f_test)


from sklearn.preprocessing import MinMaxScaler
mmc=MinMaxScaler()

f2_train=mmc.fit_transform(f_train)
f2_test=mmc.transform(f_test)



