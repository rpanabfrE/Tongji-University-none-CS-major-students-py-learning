# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 12:33:43 2024

@author: xieti
"""

year=int(input("输入工龄："))
foundation=year*1000

rank=str(input("输入等级："))
while rank!="A" and rank!="B" and rank!="C":
    rank=str(input("等级格式错误！请重新输入等级："))
    
if rank=="A":
    x=1.3
elif rank=="B":
    x=1.15
elif rank=="C":
    x=1.05
    
money=foundation*x
print("年终奖金为：",money)