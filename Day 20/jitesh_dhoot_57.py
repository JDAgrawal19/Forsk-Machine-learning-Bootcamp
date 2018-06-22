# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 10:24:39 2018

@author: JITESH
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
data=pd.read_csv("affairs.csv")
feature=data.iloc[:,0:8].values
label=data.iloc[:,8].values


print "% of women who has affair",data['affair'].value_counts(normalize=True)

from sklearn.preprocessing import OneHotEncoder
for i in [-2,-1]:
    onehot_encoder=OneHotEncoder(categorical_features=[i])
    feature=onehot_encoder.fit_transform(feature).toarray()
    feature = feature[:,1:]



#feature=np.delete(feature,0,1)
#feature=np.delete(feature,6,1)


from sklearn.model_selection import train_test_split
f_train,f_test,y_train,y_test=train_test_split(feature,label,test_size=0.2,random_state=0)

from sklearn.linear_model import LogisticRegression
classifier=LogisticRegression(random_state=0)
classifier.fit(f_train,y_train)

labels_pred_logistic=classifier.predict(f_test)

from sklearn.metrics import confusion_matrix

cm_logistic=confusion_matrix(y_test,labels_pred_logistic)

classification_score=classifier.score(f_test,y_test)


"""3,25,3,1,4,16,4,2]

list1=np.array(list1)
list1=list1.reshape(1,-1)
list1=onehot_encoder.transform(list1).toarray()
list1=np.delete(list1,0,1)
list1=np.delete(list1,6,1)


classifier.predict(list1)
"""


from sklearn.neighbors import KNeighborsClassifier
classifier_knn=KNeighborsClassifier(n_neighbors=5,p=2)

classifier_knn.fit(f_train,y_train)

pred_labels=classifier_knn.predict(f_test)

from sklearn.metrics import confusion_matrix
cm=confusion_matrix(y_test,pred_labels)


score=classifier_knn.score(f_test,y_test)







import statsmodels.formula.api as sm    

feature=np.append(arr=np.ones((6366,1)).astype(int),values=feature,axis=1)
feature_opt=feature[:,[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]]
classifier_OLS=sm.OLS(endog=label,exog=feature_opt).fit()
classifier_OLS.summary()

"""from matplotlib.colors import ListedColormap

features_set,labels_set=f_train,y_train

features1,features2=np.meshgrid(np.arange(start=features_set[:,0].min()-1,stop=features_set[:,0] .max()+1,step=0.01),
                              np.arange(start=features_set[:,1].min()-1,stop=features_set[:,1] .max()+1,step=0.01))

plt.contourf(features1,features2,classifier.predict(np.array([features1.ravel(),features2.ravel()]).T).reshape(features1.shape),
                                                              alpha=0.75,cmap=ListedColormap(('red','green')))


plt.xlim(features1.min(),features1.max())
plt.ylim(features1.min(),features2.max())
for i,j in enumerate(np.unique(labels_set)):
    plt.scatter(features_set[labels_set==j,0],features_set[labels_set==j,1],
                c=ListedColormap(('red','green'))(i),label=j)

plt.title('Logistic Regression(Test set)')
plt.featureslabel('Age')
plt.ylabel('Estimated salary')
plt.legend()
plt.show()

"""


















