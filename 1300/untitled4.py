# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 00:42:34 2023

@author: risha
"""

n=int(input())
a=list(map(int,input().split()))
m=int(input())
b=list(map(int,input().split()))
g=[]
for i in range(n):
    for j in range(m):
        if b[j]%a[i]==0:
            g.append(b[j]/a[i])
print(g.count(max(g)))