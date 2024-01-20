# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 20:05:49 2023

@author: risha
"""

for i in range(int(input())):
    n=int(input())
    s=list(input())
    us=set(s)
    c=0
    for j in us:
        if s.count(j)>=(ord(j)-64):
            c+=1
    print(c)