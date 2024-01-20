# -*- coding: utf-8 -*-
"""
Created on Sat Jan 13 00:36:00 2024

@author: risha
"""

n=int(input())
b=list(map(int,input().split()))
dif=max(b)-min(b)
c=set(b)
if len(c)==1:
    print(dif,n*(n-1)//2)
else:
    print(dif,b.count(max(b))*b.count(min(b)))