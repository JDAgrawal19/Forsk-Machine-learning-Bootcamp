# -*- coding: utf-8 -*-
"""
Created on Tue May 29 11:14:02 2018

@author: JITESH
"""

import pandas as pd
data=pd.read_csv("Loan.csv")
features=data.iloc[:,:-1].values
label=data.iloc[:,-1].values


#features_df=pd.DataFrame(features)
#label_df=pd.DataFrame(label)


from sklearn.preprocessing import LabelEncoder,OneHotEncoder
label_encoder=LabelEncoder()


features[:,1]=label_encoder.fit_transform(features[:,1])
features[:,2]=label_encoder.fit_transform(features[:,2])
features[:,3]=label_encoder.fit_transform(features[:,3])
features[:,4]=label_encoder.fit_transform(features[:,4])
features[:,5]=label_encoder.fit_transform(features[:,5])
features[:,11]=label_encoder.fit_transform(features[:,11])
features[:,0]=label_encoder.fit_transform(features[:,0])


#features_df=pd.DataFrame(features)
onehot_encoder=OneHotEncoder(categorical_features=[11])
features=onehot_encoder.fit_transform(features).toarray()


label=label_encoder.fit_transform(label)

#features_df_1=pd.DataFrame(features)
#label_df_1=pd.DataFrame(label)


from sklearn.model_selection import train_test_split
features_train,features_test,label_train,label_test=train_test_split(features,label,test_size=0.2,random_state=0)


