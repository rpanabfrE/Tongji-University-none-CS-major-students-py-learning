# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

sum=1
for i in range (1000,10000):
    i=str(i)
    a=int(i[0])
    b=int(i[1])
    c=int(i[2])
    d=int(i[3])
    i=int(i)
    if a**4+b**4+c**4+d**4==i:
        print("我找到的第",sum,"个四叶玫瑰数是：",i)
        sum += 1