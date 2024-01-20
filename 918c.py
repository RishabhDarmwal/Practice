# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 20:19:00 2023

@author: risha
"""
import math 
for i in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    s=sum(a) 
    sqrt_num = math.sqrt(s)  
    if sqrt_num.is_integer():  
        print("YES")
    else:
        print("NO")