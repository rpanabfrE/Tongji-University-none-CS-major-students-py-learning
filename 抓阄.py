# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 23:35:33 2024

@author: xieti
"""

import numpy as np

data = list(range(1,10))  # 导入待排序的所有号码，此处例为data = [1,2,3,4,5,6,7,8,9]，可修改 

np.random.shuffle(data)  # 随机排序

print("现随机排序为：",data)



#----------分割线----------



import random

x=random.randint(1,50)

print("随机抽取的号码为：",x)