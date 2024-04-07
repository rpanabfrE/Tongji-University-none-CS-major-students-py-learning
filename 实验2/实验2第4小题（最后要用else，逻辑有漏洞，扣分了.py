# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 13:29:10 2023

@author: xieti
"""

x=int(input("请输入金额："))

if x<1000:
    y=x
elif 1000<=x<2000:
    y=0.9*x
elif 2000<=x<3000:
    y=0.8*x
else:
    y=0.7*x
    
print("应付价为：",y)