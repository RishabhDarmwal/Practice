# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 00:49:41 2023

@author: risha
"""

n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
 
pos = {}
for i in range(n):
    pos[a[i]] = i + 1
 
vasya_comparisons = 0
petya_comparisons = 0
for i in range(m):
    vasya_comparisons += pos[b[i]]
    petya_comparisons += n - pos[b[i]] + 1
 
print(vasya_comparisons, petya_comparisons)
