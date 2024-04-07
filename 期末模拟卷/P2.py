# -*- coding: utf-8 -*-
"""
Created on Sat Dec 23 16:06:50 2023

@author: xieti
"""

n=int(input("请输入项数："))
i=1
ans=0

while i<=2*n-1:
    a=1/(i*(i+1))
    ans+=a                        # ans = ans + a
    i+=2                          # i = i + 2

print("前",n,"项的和为：",ans)