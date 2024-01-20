# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 19:27:35 2024

@author: risha
"""

s=input()
ss=set(s)
c=0
for i in ss:
    if s.count(i)%2==1:
        c+=1
if c==0:
    print('First')
elif c==1:
    print('First')
elif c%2==1:
    print('First')
elif c%2==0 :
    print('Second')
