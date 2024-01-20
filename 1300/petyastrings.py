# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 23:07:21 2023

@author: risha
"""

s1=list(input().lower())
s2=list(input().lower())
c=0
for i in range(len(s1)):
    if s1[i]==s2[i]:
        c=1
    else:
        if s1[i]<s2[i]:
            print("-1")

        elif s1[i]>s2[i]:
                print("1")
        c=0
        break
if c==1:
    print(0)
