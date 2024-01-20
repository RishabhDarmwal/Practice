# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 21:13:58 2024

@author: risha
"""

for i in range(int(input())):
    n,m=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    an=sorted(a)
    bn=sorted(b)
    d=0
    for j in range(n):
        if n%2==1 and j==n-1:
            d+=max(abs(bn[int(-j/2-1)]-an[int(j/2)]),bn[int((j-1)/2)]-an[int((-j-1)/2)])
        elif j%2==0:
            d+=abs(bn[int(-j/2-1)]-an[int(j/2)])
        else:
            d+=abs(bn[int((j-1)/2)]-an[int((-j-1)/2)])

    print(d)
        