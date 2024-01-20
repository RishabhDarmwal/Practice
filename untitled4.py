# -*- coding: utf-8 -*-
"""
Created on Wed Dec 27 20:41:39 2023

@author: risha
"""
import sys

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    c = 0
    min_element = float('inf')  # Track current minimum
    for i in range(1, n):
        if a[i] < min_element:  # Inversion found
            c += i
        min_element = min(min_element, a[i])
    print(c)