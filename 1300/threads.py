# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 20:33:34 2023

@author: risha
"""

for i in range(int(input())):
    c=0
    a=list(map(int,input().split()))
    a.sort()
    t=0
    while c<3:
        for i in a:
            s=set(a)
            if len(s)==1:
                t=1
            else:
                t=0
                break
        if t==1:
            print("YES")
            break
        c+=1
        r=a[-1]-a[0]
        a[-1]=a[0]
        a.append(r)
        a.sort()
    s=set(a)
    if len(s)==1 and t!=1:
        print('YES')
    elif len(s)!=1:
        print("NO")
        