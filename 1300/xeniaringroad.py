# -*- coding: utf-8 -*-
"""
Created on Sun Oct  8 23:28:25 2023

@author: risha
"""

n,m=map(int,input().split())
a=list(map(int,input().split()))
c=0
cr=1
for i in range(len(a)):
    if a[i]>=cr:
        c+=a[i]-cr
        cr=a[i]
    else:
        c+=n+a[i]-cr
        cr=a[i]
print(c)