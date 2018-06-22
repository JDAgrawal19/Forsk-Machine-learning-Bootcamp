# -*- coding: utf-8 -*-
"""
Created on Mon Jun 18 11:19:58 2018

@author: JITESH
"""

import pandas as pd

data=pd.read_csv("movie.csv")

import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

corpus=[]
for i in range(0,2000):
    review=re.sub('[^a-zA-Z]',' ',data['text'][i])
    review=review.lower()
    review=review.split()
    ps=PorterStemmer()
    review=[ps.stem(word) for word in review if not word in set(stopwords.words('english'))]
    review=' '.join(review)
    corpus.append(review)


from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features = 1500)
features = cv.fit_transform(corpus).toarray()
labels = data.iloc[:, 0].values

from sklearn.preprocessing import LabelEncoder
labelencode=LabelEncoder()

labels=labelencode.fit_transform(labels)

from sklearn.cross_validation import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.20, random_state = 0)

import sklearn.naive_bayes as nv 
classifier1 =nv.BernoulliNB()
classifier2=nv.GaussianNB()
classifier1.fit(features_train, labels_train)
classifier2.fit(features_train,labels_train)

labels_pred_1 = classifier1.predict(features_test)
labels_pred_1=labels_pred_1.reshape(-1,1)


labels_pred_2 = classifier2.predict(features_test)
labels_pred_2=labels_pred_2.reshape(-1,1)


labels_test=labels_test.reshape(-1,1)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix, accuracy_score
cm1 = confusion_matrix(labels_test, labels_pred_1)

cm2=confusion_matrix(labels_test,labels_pred_2)


score1=accuracy_score(labels_test,labels_pred_1)

score2=accuracy_score(labels_test,labels_pred_2)