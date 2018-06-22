# -*- coding: utf-8 -*-
"""
Created on Mon Jun  4 10:23:42 2018

@author: JITESH
"""
import matplotlib.pyplot as plt
import numpy as np

import pandas as pd
data=pd.read_csv("bluegills.csv")
age=data.iloc[:,0:1].values
length=data.iloc[:,1].values

from sklearn.linear_model import LinearRegression
regressor=LinearRegression()
regressor.fit(age,length)


plt.scatter(age,length,color='red')
plt.plot(age,regressor.predict(age),color='blue')
plt.title('age vs length')
plt.xlabel('age')
plt.ylabel('length')
plt.show()

from sklearn.preprocessing import PolynomialFeatures
poln_object=PolynomialFeatures(degree=2)

poly_age=poln_object.fit_transform(age)


poly_regressor=LinearRegression()
poly_regressor.fit(poly_age,length)



plt.scatter(age,length,color='red')
plt.plot(age,poly_regressor.predict(poly_age),color='blue')
plt.title('age vs length')
plt.xlabel('age')
plt.ylabel('length')
plt.show()


feature_grid=np.arange(min(age),max(age),0.1)
feature_grid=feature_grid.reshape(-1,1)
plt.scatter(age,length,color='red')
plt.plot(feature_grid,poly_regressor.predict(poln_object.fit_transform(feature_grid)),color='blue')
plt.show()


regressor.predict(7)
poly_regressor.predict(poln_object.fit_transform(7))























