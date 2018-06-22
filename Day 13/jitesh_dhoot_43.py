# -*- coding: utf-8 -*-
"""
Created on Mon May 28 11:53:40 2018

@author: JITESH
"""

import pandas as pd

data=pd.read_csv("Automobile.csv")


x=data['make'].value_counts()

car_makers=list(x.index)


import matplotlib.pyplot as plt
pie_c=plt.subplot()

labels=car_makers
sizes=x
explode=[0]*22
explode[0]=0.1

pie_c.pie(sizes[0:10],labels=labels[0:10],autopct='%1.2f%%',explode=explode[0:10])
