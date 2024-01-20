# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 20:27:52 2023

@author: risha
"""
def delUp(st):
    for i in reversed(range(len(st))):
        if st[i].isupper():
            return st[:i]+st[i+1:]
            break
    else:
        return st
def delLow(st):
    for i in reversed(range(len(st))):
        if st[i].islower():
            return st[:i]+st[i+1:]
            break
    else:
        return st
        
for j in range(int(input())):
    s=list(input())
    ns=''
    for i in s:
        if i=='B':
            ns=delUp(ns)
        elif i=='b':
            ns=delLow(ns)
        else:
            ns=ns+i
    print(ns)