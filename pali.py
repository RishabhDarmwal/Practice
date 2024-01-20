# -*- coding: utf-8 -*-
"""
Created on Sun Oct 22 16:43:01 2023

@author: risha
"""

for i in range(int(input())):
        n,k=map(int,(input().split()))
        s=input()
        x=set(s)
        odd=0
        odds=[]
        for j in x:
            if s.count(j)%2==1:
                odd+=1
                if odd==1:
                    continue
                odds.append(s.count(j))
        if len(s)-k==1:
            print("YES")
        elif odd>1:
            diff=sum(odds)
            
            if diff<=k :
                print("YES")
            else:
                print("NO")
        else:
            print("YES")
        
