# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 22:57:09 2018

@author: JITESH
"""
import pandas as pd
import project_delhi_exp as delhi
labels=pd.DataFrame(delhi.data[['tempC','MAX_TEMP_C','MIN_TEMP_C','humidity']])
labels=labels.iloc[:,0:].values

labels_df=pd.DataFrame(labels)

import project_baghpat as baghpat
import project_faridabad as faridabad
import project_gaziadabad as gaziabad
import project_gurgaon as gurgaon
import project_rohtak as rohtak
import project_sonipat as sonipat


temp_baghpat= pd.DataFrame(baghpat.data[['Date','tempC','MAX_TEMP_C','MIN_TEMP_C','humidity','time']])
temp_faridabad= pd.DataFrame(faridabad.data[['tempC','MAX_TEMP_C','MIN_TEMP_C','humidity']])
temp_gaziabad= pd.DataFrame(gaziabad.data[['tempC','MAX_TEMP_C','MIN_TEMP_C','humidity']])
temp_gurgaon= pd.DataFrame(gurgaon.data[['tempC','MAX_TEMP_C','MIN_TEMP_C','humidity']])
temp_rohtak= pd.DataFrame(rohtak.data[['tempC','MAX_TEMP_C','MIN_TEMP_C','humidity']])
temp_sonipat= pd.DataFrame(sonipat.data[['tempC','MAX_TEMP_C','MIN_TEMP_C','humidity']])


feature_df=pd.concat([temp_baghpat,temp_faridabad,temp_gaziabad,temp_gurgaon,temp_rohtak,temp_sonipat],axis=1)
feature=feature_df.iloc[:,1:].values


from sklearn.model_selection import train_test_split
f_train,f_test,l_train,l_test=train_test_split(feature,labels,test_size=0.4,random_state=0)



from sklearn.linear_model import LinearRegression
regressor=LinearRegression()

regressor.fit(f_train,l_train)

labels_pred=regressor.predict(f_test)

score=regressor.score(f_test,l_test)

#2018-06-20
l1=[37,43,35,28,0,39,45,37,25,39,45,36,26,40,45,38,26,38,44,36,29,37,43,35,28]
import numpy as np
array=np.asarray(l1)
delhi_predict_l1=regressor.predict(array.reshape(1,-1))

#2018-06-21
l2=[40,43,36,30,714,41,44,39,21,41,44,39,21,41,43,39,28,41,43,38,28,41,43,36,28]
array1=np.asarray(l2)
delhi_today=regressor.predict(array1.reshape(1,-1))

from sklearn.model_selection import cross_val_score
accuracies = cross_val_score(estimator = regressor, X = f_train, y = l_train, cv = 10)
print ("mean accuracy is",accuracies.mean())
print (accuracies.std())





