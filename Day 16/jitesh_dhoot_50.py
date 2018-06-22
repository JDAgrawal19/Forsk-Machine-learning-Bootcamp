# -*- coding: utf-8 -*-
"""
Created on Thu May 31 10:54:08 2018

@author: JITESH
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


data=pd.read_csv("Foodtruck.csv")
population=data.iloc[:,:-1].values
profit=data.iloc[:,-1].values


from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(population,profit,test_size=0.2,random_state=0)

from sklearn.linear_model import LinearRegression
regressor=LinearRegression()
regressor.fit(x_train,y_train)


profit_pred=regressor.predict(x_test)

score=regressor.score(x_test,y_test)

plt.scatter(x_train,y_train,color='red')
plt.plot(x_train,regressor.predict(x_train),color='blue')
plt.title('profit vs population training')
plt.xlabel('population')
plt.ylabel('profit')
plt.show()



plt.scatter(x_test,y_test,color='red')
plt.plot(x_train,regressor.predict(x_train),color='blue')
plt.title('profit vs population test')
plt.xlabel('population')
plt.ylabel('profit')
plt.show()


jaipur_profit=regressor.predict(3.073)