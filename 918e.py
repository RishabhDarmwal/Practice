# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 21:03:04 2023

@author: risha
"""

for i in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    c=0
    for i in range(2,n+1):
        for j in range(n-i+1):
            x=a[j:j+i]
            if sum(x[0::2])==sum(x[1::2]):
                print("YES")
                c=1
                break
        if c==1:
            break
    else:
        print("NO")
        