# -*- coding: utf-8 -*-
"""
Created on Sun Oct 22 16:36:05 2023

@author: risha
"""

for i in range(int(input())):
    s=input()
    c=0
    p=1
    for j in range(len(s)):
        if s[j]=='0':
            x=10
        else:
            x=int(s[j])
        c+=abs(x-p)+1
        p=x
    print(c)