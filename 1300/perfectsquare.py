# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 20:53:22 2023

@author: risha
"""

for i in range(int(input())):
    p=0
    n=int(input())
    m=[]
    for j in range(n):
        r=list(input())
        m.append(r)
    c=0                        
    for k in range(n):
        for j in range(n):
            if m[k][j]!=m[k][n-1-j]:
                if m[k][j]<m[k][n-1-j]:
                    c+=ord(m[k][n-1-j])-ord(m[k][j])
                    m[k][j]=m[k][n-1-j]
                else:
                    c+=ord(m[k][j])-ord(m[k][n-1-j])
                    m[k][n-1-j]=m[k][j]
    print(c)
            

            