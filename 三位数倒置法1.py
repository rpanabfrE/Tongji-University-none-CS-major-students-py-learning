# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# //与 %

x=int(input("请输入一个三位数："))
if 100<=x<=999:
    a=x//100
    b=x//10%10
    c=x%10
    y=c*100+b*10+a
    print("倒置后的三位数为：",y)
else:
    print("错误！输入的不是三位数")