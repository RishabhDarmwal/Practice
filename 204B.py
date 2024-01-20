# -*- coding: utf-8 -*-
"""
Created on Sun Jan 14 23:35:07 2024

@author: risha
"""
n=int(input())
a = [int(x) for x in input().split()] 
s={}  #{ Element : (current index, difference b/n current &last index)}
for i in range(n):
    m=a[i]
    if m in s:          #a[m][1]=0 means it occured only once yet 
        s[m]=(i,-1 if s[m][1] and i-s[m][0]!=s[m][1] else i-s[m][0])
        #        not AP if curr dif!=prev diff  else if eq 
    else: #if new element
        s[m]=(i,0) 

b=[(p,s[p][1]) for p in sorted(s.keys()) if s[p][1]>=0]
print(len(b))
for i in b:
    print(i[0],i[1])

        