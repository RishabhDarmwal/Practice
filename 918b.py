# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 20:09:52 2023

@author: risha
"""
l={'A','B','C'}
for i in range(int(input())):    
    a=set(input())
    b=set(input())
    c=set(input())
    if '?' in a:
        x=(l-a).pop()
        print(x)
    elif '?' in b:
        x=(l-b).pop()
        print(x)
    elif '?' in c:
        x=(l-c).pop()
        print(x)