# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 15:55:25 2023

@author: risha
"""

a,b,c=map(int,input().split())
x=(a*c/b)**0.5
y=(a*b/c)**0.5
z=(b*c/a)**0.5
print(4*int(x+y+z))