# -*- coding: utf-8 -*-
"""
Created on Sun Oct  1 23:35:11 2023

@author: risha
"""
#lightsout
r1=list(map(int,input().split()))
r2=list(map(int,input().split()))
r3=list(map(int,input().split()))
T=[r1,r2,r3]
def sumrem(s,t):
    sum=0
    if 0<=s-1:
        sum+=T[s-1][t]%2
    if s+1<=2:
        sum+=T[s+1][t]%2
    if 0<=t-1:
        sum+=T[s][t-1]%2
    if t+1<=2:
        sum+=T[s][t+1]%2
    sum+=T[s][t]%2
    return sum%2
    
G=[['1','1','1'],['1','1','1'],['1','1','1']]
for i in range(3):
    for j in range(3):
            if sumrem(i,j)==1:
                G[i][j]='0'
for p in range(3): 
    for q in range(3):
        print(G[p][q],end='') 
    print()