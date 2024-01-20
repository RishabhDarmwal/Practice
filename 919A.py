# -*- coding: utf-8 -*-
"""
Created on Sat Jan 13 20:31:25 2024

@author: risha
"""

for i in range(int(input())):
    n=int(input())
    mn=float('-inf')
    mx=float('inf')
    ex=[]
    for j in range(n):
        a,x=map(int,input().split())
        if a==1:
            if x>mn:
                mn=x
        elif a==2:
            if x<mx:
                mx=x
        elif a==3:
            print(3, x)
            ex.append(x)
    for p in ex:
        if p<=mn or p>=mx:
            ex.remove(p)
    if mn>mx:
        print(0)
    elif mx-mn==1:
        if (mx in ex and mn not in ex) or (mx not in ex and mn in ex):
            print(1)
        elif mx in ex and mn in ex:
            print(0)
        else:
            print(2)
    else:
        print(mx-mn+1-len(ex))
