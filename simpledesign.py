# -*- coding: utf-8 -*-
"""
Created on Sun Oct 22 14:25:11 2023

@author: risha
"""

for i in range(int(input())):
    x,k=map(int,input().split())
    f=0    
    while f==0:
            y=str(x)
            c=0
            for j in range(len(y)):
                c+=int(y[j])
            if c%k==0:
                f=1
            else:
                x+=1
    print(x)