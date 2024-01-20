# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 00:13:04 2023

@author: risha
"""

n=int(input())
l=list(map(int,input().split()))
i=0;c=0
while n>0:
    n-=l[i]
    i+=1
    c+=1
    if i>6:
        i=0
if c%7==0:
    print(7)
else:
    print(c%7)
