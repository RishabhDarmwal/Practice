# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 22:54:00 2023

@author: risha
"""

k=int(input())
s=input()
z=set(s)
d=[]
e=[]
for i in z:
    if s.count(i)%k!=0:
        print(-1)
        break
    else:
        c=s.count(i)//k
        d.append(c)
        e.append(i)
else:
    ss=''
    ite=len(s)//sum(d)
    while d!=[]:
        a=d.pop()
        b=e.pop()
        ss+=b*a
    print(ss*ite)
        