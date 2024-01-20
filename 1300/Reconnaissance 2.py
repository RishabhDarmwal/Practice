# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 23:17:31 2023

@author: risha
"""

n=int(input())
l = list(map(int, input().split()))
end=l[0]
l.append(end)
diff=abs(l[0]-l[1])
a,b=1,2
for i in range(1,n):
    d=abs(l[i]-l[i+1])
    if d<diff:
        diff=d
        a,b=i+1,i+2
    if a==n:
        b=1
print(a,b)