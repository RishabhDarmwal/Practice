# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 22:22:31 2023

@author: risha
"""
def inorder(lst):
    for i in range(len(lst)-1):
        if lst[i]>lst[i+1]:
            return 0
            break
    else:
        return 1

    
for i in range(int(input())):
    n,k=map(int,input().split())
    l=list(map(int,input().split()))
    if inorder(l):
        print("YES")
    elif k==1:
        print("NO")
    else:
        print("YES")
    
    