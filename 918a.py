# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 20:06:04 2023

@author: risha
"""

for i in range(int(input())):
    a=list(map(int,input().split()))
    for j in a:
        if a.count(j)==1:
            print(j)
            break