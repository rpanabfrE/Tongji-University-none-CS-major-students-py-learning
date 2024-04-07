# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 09:28:19 2024

@author: xieti
"""

import numpy as np
from sklearn.linear_model import LinearRegression

X=np.array([1727.2,1949.8,2187.9,2436.1,2663.7,2889.1,3111.9,3323.1,3529.3,3789.7])
X=X.reshape(-1,1)
y=np.array([861.4,966.6,1048.6,1108.7,1213.1,1322.8,1380.9,1460.6,1564.4,1690.8])

lr=LinearRegression()
lr.fit(X,y)

new_X=np.array([10000])
new_X=new_X.reshape(-1,1)
print("GDP为10000时人均消费支出估计为：",lr.predict(new_X))