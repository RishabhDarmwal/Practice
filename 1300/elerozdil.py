# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 23:39:44 2023

@author: risha
"""

n=int(input())
l=list(map(int,input().split()))
m=min(l)
c=l.index(m)+1
l.remove(m)
if m in l:
    print("Still Rozdil")
else: 
    print(c)
