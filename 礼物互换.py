# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 20:25:19 2024

@author: xieti
"""

import random
import numpy as np

data = list(range(1,50))  # 导入待排序的所有号码，data可修改 
np.random.shuffle(data)   # 随机排序

print("抽签规则为：前一号码与后一号码配一组")
print("现随机排序为：",data)