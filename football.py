# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 15:54:25 2023

@author: risha
"""

s=input()
if len(s)<7:
    print("NO")
else:
    for i in range(len(s)-6):
        for j in range(1,7):
            if s[i+j]!=s[i]:
                f=0
                break                
        else:            
            f=1
        if f==1:
            break
    if f==1:
        print("YES")
    else:
        print("NO")