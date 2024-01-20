# -*- coding: utf-8 -*-
"""
Created on Sat Oct 14 01:48:15 2023

@author: risha
"""

n,m=map(int,input().split())
a=list(map(int,input().split()))

s=0
a.sort()
for i in range(m):
    if a[i]<0:
        s+=a[i]
    else:
        break
print(abs(s))