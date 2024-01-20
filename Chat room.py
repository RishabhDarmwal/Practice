# -*- coding: utf-8 -*-
"""
Created on Sat Dec 23 11:42:39 2023

@author: risha
"""

s=input()
i=0;c=0
while i<len(s):
    if s[i]=='h' and c==0:
        c+=1
    elif s[i]=='e' and c==1:
        c+=1
    elif s[i]=='l' and c==2:
        c+=1
    elif s[i]=='l' and c==3:
        c+=1
    elif s[i]=='o' and c==4:
        c+=1
    i+=1
if c==5:
    print("YES")
else:
    print("NO")
    
        
        
        