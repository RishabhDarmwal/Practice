# -*- coding: utf-8 -*-
"""
Created on Sat Oct 14 01:38:32 2023

@author: risha
"""

k=int(input())
a=list(map(int,input().split()))
a.sort()
c=0
g=0
while k>g:
    if c==12:
        print(-1)
        break
    m=a.pop()
    g+=m
    c+=1
else:
    print(c)