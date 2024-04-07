# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 19:40:59 2023

@author: xieti
"""

from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

iris=datasets.load_iris() 			    # 获取鸢尾花数据集
X=iris.data 				    # 获取鸢尾花特征矩阵
y=iris.target  				    # 获取鸢尾花目标数组
Xtrain,Xtest,ytrain,ytest=train_test_split(X,y,random_state=0)  # 分成训练集和测试集

knn = KNeighborsClassifier(n_neighbors=3)   # 初始化模型
knn.fit(Xtrain,ytrain)

score=knn.score(Xtest,ytest)	                 # 测试模型
print("准确率：",score)

y_sample=knn.predict([[1,2,3,4]])		    # 进行预测
print("预测结果：",y_sample)