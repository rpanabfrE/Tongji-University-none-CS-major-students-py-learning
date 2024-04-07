# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from math import *

a=float(input("请输入直角三角形的斜边a："))
b=float(input("请输入直角三角形的一条直角边b："))

if a>b:
    c=sqrt(a**2-b**2) #求直角三角形的另外一条直角边c
    L=a+b+c #求直角三角形的周长L
    S=(b*c)/2 #求直角三角形的面积S
    print("直角三角形另外一条直角边的长为",c,"直角三角形的周长为",L,"直角三角形的面积为",S)
else:
    print("所输入的边长不符合直角三角形性质")