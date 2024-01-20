# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 19:12:49 2024

@author: risha
"""

n,h=map(int,input().split())
a=list(map(int,input().split()))
c=0
for x in a:
    if x>h:
        c+=2
    else:
        c+=1
print(c)