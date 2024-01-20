# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 20:19:43 2023

@author: risha
"""

def delUp(st):
    for i in reversed(range(len(st))):
        if st[i].isupper():
            print(1)
            return st[:i]+st[i+1:]
            break
    else:
        return st
def delLow(st):
    for i in reversed(range(len(st))):
        print(1)
        if st[i].islower():
            print(1)
            return st[:i]+st[i+1:]
            break
    else:
        print(2)
        return st
print(delLow('A'))