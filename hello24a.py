# -*- coding: utf-8 -*-
"""
Created on Sat Jan  6 20:17:56 2024

@author: risha
"""

for i in range(int(input())):
    a,b=map(int,input().split())
    if (a+b)%2:
        print("Alice")
    else:
        print("Bob")