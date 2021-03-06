# -*- coding: utf-8 -*-
"""ML_hierarchical.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1cp0Kby2fMgxkLI_gjFoMAs0_HdGQ-KwT
"""

from google.colab import drive

drive.mount('/content/drive')

cd /content/drive/"MyDrive/ICT_ DEGREE/sem 6/ML"

ls

import numpy as np
import pandas as pd #panda used as csv file to convert into dataframe lib is used '''
import matplotlib.pyplot as plt #mathematical plotting library python plots'''

dataset = pd.read_csv("KMeans.csv")

dataset

X=dataset.iloc[:,[1,2]].values

X.shape

import scipy.cluster.hierarchy as sch

dendrogram=sch.dendrogram(sch.linkage(X,method='ward'))#conveting to linkage matrix
#

from sklearn.cluster import AgglomerativeClustering

hc=AgglomerativeClustering(n_clusters=5,affinity='euclidean',linkage='ward')#euclidean distance used 
#distance threshold y axis
#no of cluster = 5 so at time distance threshold not possible x axias

y_hc=hc.fit_predict(X)

y_hc

#visualizing cluster
plt.scatter(X[y_hc==0,0],X[y_hc==0,1],s=50,c='red',label='cluster 1')
plt.scatter(X[y_hc==1,0],X[y_hc==1,1],s=50,c='blue',label='cluster 2')
plt.scatter(X[y_hc==2,0],X[y_hc==2,1],s=50,c='green',label='cluster 3')
plt.scatter(X[y_hc==3,0],X[y_hc==3,1],s=50,c='yellow',label='cluster 4')
plt.scatter(X[y_hc==4,0],X[y_hc==4,1],s=50,c='black',label='cluster 5')

plt.title('hierarchical clustering')
plt.xlabel('annual income')
plt.ylabel('spending score')
plt.legend()

from sklearn.cluster import KMeans

#wcss within cluster sum of square
wcss=[]
for i in range(1,10):
  kmeans=KMeans(n_clusters=i,init='k-means++',random_state=0)
  kmeans.fit(X)
  wcss.append(kmeans.inertia_)
plt.plot(range(1,10),wcss)
plt.title('kmeans elbow graph')
plt.ylabel('wcss')
plt.xlabel('# of cluster')
plt.show()

kmeans=KMeans(n_clusters=5,init='k-means++',random_state=0)
y_kmeans=kmeans.fit_predict(X)

plt.scatter(X[y_kmeans==0,0],X[y_kmeans==0,1],s=50,c='red',label='cluster 1')
plt.scatter(X[y_kmeans==1,0],X[y_kmeans==1,1],s=50,c='blue',label='cluster 2')
plt.scatter(X[y_kmeans==2,0],X[y_kmeans==2,1],s=50,c='green',label='cluster 3')
plt.scatter(X[y_kmeans==3,0],X[y_kmeans==3,1],s=50,c='yellow',label='cluster 4')
plt.scatter(X[y_kmeans==4,0],X[y_kmeans==4,1],s=50,c='black',label='cluster 5')
plt.scatter(kmeans.cluster_centers_[:,0],kmeans.cluster_centers_[:,1],s=200,c='cyan',label='centroids')

plt.title('hierarchical clustering')
plt.xlabel('annual income')
plt.ylabel('spending score')
plt.legend()

#classification dataset 
#atleast 4 class 
#keans->elbow
#dendrogram 
#21/12/2021