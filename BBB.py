# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 20:19:00 2024

@author: risha
"""

for i in range(int(input())):
    n=int(input())
    s=input()
    f=input()
    extra=0
    tofill=0
    for i in range(n):
        
        if s[i]=='1' and f[i]=='0':
            extra+=1
        elif s[i]=='0' and f[i]=='1':
            tofill+=1
        
    print(max(tofill,extra))
                
            