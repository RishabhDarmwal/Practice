# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 22:40:02 2023

@author: risha
"""

for i in range(int(input())):
    n=int(input())
    lst=[]
    maxi=0
    for j in range(n):
        l=list(map(int,input().split()))
        if max(l)>maxi:
            maxi=max(l)
        lst.append(l)
    a=[]
    num=0
    for j in range(1,n):        
        if a==[]:
            for m in range(maxi):
                for n in range(maxi):
                    if m|n==lst[0][j]:
                        a.append(m)
                        num=m
                        break
                else:
                    break
        else:
            for n in range(maxi):
                if m|num==lst[0][j]:
                    a.append(m)
                    num=m
                    break
    if n==1:
        print("YES")
        print("7")
    elif a==[]:
        print("NO")
    else:
        print("YES")
        for i in a:
            print(i,end=' ')
        print()
    