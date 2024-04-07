# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 19:49:40 2023

@author: xieti
"""

from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans   
import matplotlib.pyplot as plt

centers=[(18,46),(66,41),(33,16)]
X,y = make_blobs(n_samples=15,centers=centers,random_state=0,cluster_std=3.7)

kmeans = KMeans(n_clusters=2)
kmeans.fit(X)

y_pred=kmeans.predict(X)
plt.scatter(X[:,0],X[:,1],c=y_pred,cmap='viridis')