# -*- coding: utf-8 -*-
"""
Created on Sun Oct 22 18:03:58 2023

@author: risha
"""
import math

def nearestPowerOf2(N):
    
    a = int(math.log2(N))
 
    
    if 2**a == N:
        return a
     
    # Return 2^(a + 1)
    return (a + 1)
for i in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    c=0
    while True:
        s=a.copy()
        s.sort()
        
        if a==s:
            break
        for j in range(n-1):
            if a[j]>a[j+1]:
                m=a[j]//a[j+1]
                d=nearestPowerOf2(m)
                a[j+1]*=d
                c+=d
                
    print(c)