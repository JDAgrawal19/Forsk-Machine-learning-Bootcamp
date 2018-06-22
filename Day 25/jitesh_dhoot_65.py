# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 11:19:38 2018

@author: JITESH
"""

import pandas as pd
import numpy as np
data=pd.read_csv("breast_cancer.csv")

features=data.iloc[:,1:10].values
label=data.iloc[:,10].values


from sklearn.preprocessing import Imputer
imputer=Imputer(missing_values='NaN',strategy='most_frequent',axis=0)
imputer=imputer.fit(features[:,:])
features[:,:]=imputer.transform(features[:,:])

from sklearn.model_selection import train_test_split
f_train,f_test,l_train,l_test=train_test_split(features,label,test_size=0.2,random_state=0)

from sklearn.svm import SVC
classifier=SVC(kernel='rbf',random_state=0)

classifier.fit(f_train,l_train)

l_predict=classifier.predict(f_test)

from sklearn.metrics import confusion_matrix
cm=confusion_matrix(l_test,l_predict)

score=classifier.score(f_test,l_test)


predict=classifier.predict(np.asarray([6,2,5,3,2,7,9,2,4]).reshape(1,-1))