# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 12:27:36 2024

@author: xieti
"""

year=int(input("输入工龄："))
rank=str(input("输入等级："))
foundation=year*1000

if rank=="A":
    x=1.3
elif rank=="B":
    x=1.15
elif rank=="C":
    x=1.05
else:
    x=0
    print("等级格式错误！奖金清零")
    
money=foundation*x
print("年终奖金为：",money)