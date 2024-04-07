# -*- coding: utf-8 -*-
"""
Created on Sat Dec 16 17:36:53 2023

@author: 蔡雨辰
"""
import math
a=99
x0=10
x1=2/3*x0+a/(3*x0**2)
while math.fabs(x1-x0)>1E-5:
    x0=x1
    x1=2/3*x0+a/(3*x0**2)
print(x1)
