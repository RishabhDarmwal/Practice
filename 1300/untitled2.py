# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 21:29:37 2023

@author: risha
"""
t = int(input())
for T in range(t):
    n = int(input())
    if n < 1 + 2 + 4 or n == 9:
        print("NO")
    else:
        print("YES")
        if n % 3 != 0:
            print(1, 2, n - 3)
        else:
            print(1, 4, n - 5)