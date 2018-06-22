# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 10:32:36 2018

@author: JITESH
"""
import numpy as np
import pandas as pd
data=pd.read_csv("mushrooms.csv")

feature=data.iloc[:,[5,21,22]].values
label=data.iloc[:,0].values

from sklearn.preprocessing import LabelEncoder,OneHotEncoder
label_encoder=LabelEncoder()


for i in range(3):
    feature[:,i]=label_encoder.fit_transform(feature[:,i])
    
    
label=label_encoder.fit_transform(label)


onehot_encoder=OneHotEncoder()
onehot_encoder=OneHotEncoder(categorical_features=[0,1,2])
feature=onehot_encoder.fit_transform(feature).toarray()


for i in [21,12,0]:
    feature=np.delete(feature,i,1)

from sklearn.model_selection import train_test_split
f_train,f_test,l_train,l_test=train_test_split(feature,label,test_size=0.2,random_state=0)


from sklearn.neighbors import KNeighborsClassifier
classifier=KNeighborsClassifier(n_neighbors=5,p=2)

classifier.fit(f_train,l_train)

pred_labels=classifier.predict(f_test)

from sklearn.metrics import confusion_matrix
cm=confusion_matrix(l_test,pred_labels)


score=classifier.score(f_test,l_test)











