# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 20:17:48 2023

@author: risha
"""

for i in range(int(input())):
    c,r=list(input())
    cs=['a','b','c','d','e','f','g','h']
    rs=['1','2','3','4','5','6','7','8']
    for p in cs:
        if p!=c:
                print(p,r,sep='')
    for q in rs:
         if q!=r:
                 print(c,q,sep='')   