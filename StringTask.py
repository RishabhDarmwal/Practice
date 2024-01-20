# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 15:58:03 2023

@author: risha
"""
s=input()
s=s.lower()
l=list(s)
a=[]
for i in l:
    if i not in ['a','e','i','o','u','y']:
        a.append(i)
p='.'.join(a)
print('.'+p)

        