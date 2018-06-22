# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 12:24:20 2018

@author: JITESH
"""

import pandas as pd

data=pd.read_csv("banknotes.csv")

feature=data.iloc[:,1:6].values
label=data.iloc[:,6].values


from sklearn.model_selection import train_test_split
f_train,f_test,l_train,l_test=train_test_split(feature,label,test_size=0.2,random_state=0)


from sklearn.preprocessing import StandardScaler
sc=StandardScaler()

f_train=sc.fit_transform(f_train)
f_test=sc.transform(f_test)

from sklearn.linear_model import LogisticRegression
classifier=LogisticRegression(random_state=0)

classifier.fit(f_train,l_train)

pred_label=classifier.predict(f_test)

from sklearn.metrics import confusion_matrix
cm=confusion_matrix(l_test,pred_label)

score=classifier.score(f_test,l_test)


from sklearn.model_selection import cross_val_score
accuracies=cross_val_score(estimator=classifier,X=f_train,y=l_train,cv=10)

print "mean accuracy is ",accuracies.mean()
print accuracies.std()
