# -*- coding: utf-8 -*-
"""
Created on Sun Dec 24 20:09:35 2023

@author: risha
"""
import math
for i in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    p=math.prod(a)
    if p>0:
        print(1)
        print(1,0)
    else:
        print(0)
    
    