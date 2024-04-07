# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 13:49:17 2023

@author: xieti
"""

x=str(input("请输入一篇文章："))
sum=0

for i in x:
    if i in "共产党":
        sum += 1
        
print("该字符串共有",sum,"个字母")