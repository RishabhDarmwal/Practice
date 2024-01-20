# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 20:05:15 2024

@author: risha
"""

for i in range(int(input())):
    s=[]
    for j in range(4):
        x,y=map(int,input().split())
        s.append((x,y))
    x=s[0][0]
    y=s[0][1]
    for j in range(1,4):
        if s[j][0]==x:
            print((s[j][1]-y)**2)
            break
        elif s[j][1]==y:
            print((s[j][0]-x)**2)
            break  
        
            
    