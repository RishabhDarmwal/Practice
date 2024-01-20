# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 23:01:48 2023

@author: risha
"""

n,a,b=map(int,input().split())
if a+b<n-1:
    print(b+1)
else:
    print(n-a)