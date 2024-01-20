# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 00:35:47 2023

@author: risha
"""
l=[]
for i in range(int(input())):
    l.append(input())
s=set(l)
mx,a=0,0
for i in s:
    if l.count(i)>mx:
        mx=l.count(i)
        a=i
print(a)