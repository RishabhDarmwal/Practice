# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 20:14:47 2023

@author: risha
"""
def reverse_sublist(lst,start,end):
    lst[start:end] = lst[start:end][::-1]
    return lst

for i in range(int(input())):
    n,k=map(int,input().split())
    x=list(range(1,n+1))    
    reverse_sublist(x,k,n)
    c=''
    for j in range(n):
        if j==n-1:
            c+=str(x[j])
        else:
            c+=str(x[j])+' '
    print(c[::-1])