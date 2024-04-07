# -*- coding: utf-8 -*-
"""
Created on Sat Dec 23 15:48:17 2023

@author: xieti
"""

x=int(input("请输入充值金额："))
a=x//2000
b=x%2000//500
c=250*a+50*b
print("赠送金额为：",c)