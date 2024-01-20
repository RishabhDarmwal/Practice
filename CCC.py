# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 20:39:20 2024

@author: risha
"""

for i in range(int(input())):
    n,f,a,b=map(int,input().split())
    m=list(map(int,input().split()))
    sent=0
    time=0
    ans="YES"
    while sent<n:
        diff=m[sent]-time
        if diff*a>b:
            used=b
        else:
            used=diff*a
        f-=used
        time=m[sent]
        sent+=1        
        if f<=0:
            ans="NO"
            break
    print(ans)
        