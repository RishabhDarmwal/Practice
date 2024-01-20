# -*- coding: utf-8 -*-
"""
Created on Sat Oct 14 04:29:28 2023

@author: risha
"""

n,m=map(int,input().split())
c=0
for a in range(0,m+1):
    for b in range(0,n+1):
        if (a**2)+b==n and a+(b**2)==m:
            c+=1
print(c)