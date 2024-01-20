# -*- coding: utf-8 -*-
"""
Created on Sat Dec 23 11:26:50 2023

@author: risha
"""

n,m=map(int,input().split())
f=list(map(int,input().split()))
f.sort()
diff=max(f)-min(f)
for i in range(m-n+1):
    if f[i+n-1]-f[i]<diff:
        diff=f[i+n-1]-f[i]
print(diff)
