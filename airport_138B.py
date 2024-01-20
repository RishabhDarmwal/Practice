# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 21:41:45 2024

@author: risha
"""

n,m=map(int,input().split())
a=list(map(int,input().split()))
mx=0
mn=0
b=a.copy()
c=a.copy()
for i in range(n):
        p=min(b)
        if p==1:
            b.remove(1)
            mn+=1
        else:
            mn+=p
            b[b.index(p)]=p-1
for i in range(n):
        p=max(c)
        mx+=p
        c[c.index(p)]=p-1
print(mx,mn)
