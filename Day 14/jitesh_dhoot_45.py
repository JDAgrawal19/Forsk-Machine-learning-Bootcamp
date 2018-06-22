# -*- coding: utf-8 -*-
"""
Created on Tue May 29 12:53:38 2018

@author: JITESH
"""

import pandas as pd
data=pd.read_csv("Automobile.csv")

for i in data.columns:
    print data[i].dtype

data1=data.select_dtypes(include=[object])

data1=data1.fillna(data1.mode())

#data1['body_style'] = data1['body_style'].astype('category')
#data1['body_style'] = data1['body_style'].cat.codes


data1['body_style'].value_counts()

nums={"sedan" :1,
"hatchback"  :2,
"wagon"   :    3,
"hardtop " :     4,
"convertible"  : 5}

data1.replace(nums,inplace=True)

#for i in data['body_style']:
#    if(i=='convertible'):
        
        
data1['drive_wheels'] = data1['drive_wheels'].astype('category')
data1['drive_wheels'] = data1['drive_wheels'].cat.codes


data1 = pd.get_dummies(data1,columns=["body_style","drive_wheels"])