# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 22:12:21 2023

@author: xieti
"""

i=1
n=2*i-1
a=1/n
ans=0

while a>1E-6:
    ans=ans+a
    i=i+1
    n=2*i-1
    a=1/n
    
print("和为：",ans)