# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 19:22:14 2023

@author: risha
"""

w=input()
l,u=0,0
for i in w:
    if i.isupper():
        u+=1
    elif i.islower():
        l+=1
if u>l:
    w=w.upper()
else:
    w=w.lower()
print(w)