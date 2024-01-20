# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 22:02:25 2024

@author: risha
"""

for i in range(int(input())):
    h,w,xa,ya,xb,yb=map(int,input().split())
    if abs(xa-xb)%2==0:
        if abs(ya-yb)>abs(xa-xb):
            print("Draw")
        else:
            print("Bob")
    else:
        if abs(ya-yb)==abs(xa-xb):
            print("Draw")
        else:
            print("Alice")