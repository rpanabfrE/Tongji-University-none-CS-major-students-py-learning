# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# 切片

x=int(input("请输入一个三位数："))
if 100<=x<=999:
    x=str(x)
    a=int(x[0])
    b=int(x[1])
    c=int(x[2])
    y=c*100+b*10+a
    print("倒置后的三位数为：",y)
else:
    print("错误！输入的不是三位数")