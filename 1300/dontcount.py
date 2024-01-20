# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 20:09:13 2023

@author: risha
"""
for i in range(int(input())):
    n,m=map(int,input().split())
    x=input()
    s=input()
    c=0
    for j in range(7):
        if s in x:
            break
        x=x*2
        c+=1
    if c==7:
        c=-1
    print(c)