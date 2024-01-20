# -*- coding: utf-8 -*-
"""
Created on Sat Jan 13 00:51:53 2024

@author: risha
"""

n,m=map(int,input().split())
c=[]
for i in range(n):
    s=input()
    c.append(s)
    
for i in range(n):    
    for j in range(m):
        p=c[i][j]
        if (i+j)%2==0:
            if p=='.':
                print('B',end='')
            else:
                print('-',end='')
        else:
            if p=='.':
                print('W',end='')
            else:
                print('-',end='')
    print()