# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 16:29:33 2023

@author: risha
"""
import math
n,k=map(int,input().split())
mid=math.ceil(n/2)
if k>mid:
    print((k-mid)*2)
else:
    print(2*k-1)n