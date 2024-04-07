# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 19:31:27 2023

@author: xieti
"""

import numpy as np
X=np.array([861.4,966.6,1048.6,1108.7,1213.1,1322.8,1380.9,1460.6,1564.4,1690.8])
X=X.reshape(-1,1)
y=np.array([1727.2,1949.8,2187.9,2436.1,2663.7,2889.1,3111.9,3323.1,3529.3,3789.7])

from sklearn.linear_model import LinearRegression
lr=LinearRegression()
lr.fit(X,y)  
print(lr.intercept_,lr.coef_)      	#输出截距和权重系数

new_X=np.array([5000])
new_X=new_X.reshape(-1,1)
print("人均消费支出为5000时的人均GDP为:",lr.predict(new_X))