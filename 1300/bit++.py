# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 23:13:20 2023

@author: risha
"""
x=0
n=int(input())
for i in range(n):
    s=input()
    if s=='X++' or s=='++X':
        x+=1
    elif s=='X--' or s=='--X':
        x-=1
print(x)
