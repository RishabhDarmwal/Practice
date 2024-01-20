# -*- coding: utf-8 -*-
"""
Created on Sat Dec 23 11:14:33 2023

@author: risha
"""

s,n=map(int,input().split())
ds=[]

for i in range(n):
    x,y=map(int,input().split())
    ds.append([x,y])
ds.sort()     
for i in range(n):
    if s>ds[i][0]:
        s+=ds[i][1]
    else:
        print("NO")
        break
else:
    print("YES")
            
            
        