# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 22:46:53 2023

@author: risha
"""

n,k,l,c,d,p,nl,np=map((int,input().split()))
drink=l//nl
lime=c*d
salt=p//np
print(min(drink,lime,salt)//n)