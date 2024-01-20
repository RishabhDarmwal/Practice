# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 00:26:25 2023

@author: risha
"""

n,m=map(int,input().split())
l=list(map(int,input().split()))

d,r=0,0
for i in range(n):
    if l[i]%m==0:
        x=l[i]//m
    else:
        x=l[i]//m+1
    if r<=x: 
        r=x
        d=i
    
print(d+1)
