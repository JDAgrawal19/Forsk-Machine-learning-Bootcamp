# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 11:01:41 2018

@author: JITESH
"""
import matplotlib.pyplot as plt
import pandas as pd

data=pd.read_csv("crime_data.csv")
features=data.iloc[:,[1,2,4]].values


from sklearn.decomposition import PCA
pca=PCA(n_components=2)
features=pca.fit_transform(features)

explained_variance=pca.explained_variance_ratio_


from sklearn.cluster import KMeans
wcss=[]
for i in range(1,11):
    kmeans=KMeans(n_clusters=i,init='k-means++',random_state=0)
    kmeans.fit(features)
    wcss.append(kmeans.inertia_)
    
plt.plot(range(1,11),wcss)


kmeans=KMeans(n_clusters=3,init='k-means++',random_state=0)
y_kmeans=kmeans.fit_predict(features)


plt.scatter(features[y_kmeans==0,0],features[y_kmeans==0,1],s=100,c='red',label='cluster 1')
plt.scatter(features[y_kmeans==1,0],features[y_kmeans==1,1],s=100,c='blue',label='cluster 2')
plt.scatter(features[y_kmeans==2,0],features[y_kmeans==2,1],s=100,c='green',label='cluster 3')

plt.scatter(kmeans.cluster_centers_[:,0],kmeans.cluster_centers_[:,1],s=300,c='black',label='Centroids')
plt.legend()
plt.show()











