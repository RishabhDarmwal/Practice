# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 20:30:37 2023

@author: risha
"""

for i in range(int(input())):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    done=[]
    f=0
    c=0
    if k>n:
        end=0
        for i in range(k):
            r=k-i-1
            if f==n:
                end=1
            if end==0:
                if done==[]:
                    
                    done.append(b[f])
                    c+=a[f]
                    f+=1
                
                elif a[f]>max(done) or (a[f]==max(done) and b[f]>max(done)) :  
                    
                    done.append(b[f])
                    c+=a[f]
                    f+=1
                    
                elif (max(a[f:f+r])>max(done)):
                   
                    done.append(b[f])
                    c+=a[f]
                    f+=1
                    
            else:
               
                c+=max(done)
               
    else:
        for i in range(k):
            if done==[]:
                done.append(b[f])
                c+=a[f]
                f+=1
            elif a[f]>max(done) or (a[f]==max(done) and b[f]>max(done)) :  
                done.append(b[f])
                c+=a[f]
                f+=1
            else:
                c+=max(done)
            
    print(c)