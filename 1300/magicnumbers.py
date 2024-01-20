# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 00:05:53 2023

@author: risha
"""
c=1
s=input()
for i in s:
    if i!= '1' and i != '4':
        c=0
if s[0]=='4':
    c=0
if '444' in s:
    c=0
if c==1:
    print("YES")
else:
    print("NO")