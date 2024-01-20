# -*- coding: utf-8 -*-
"""
Created on Sat Jan  6 20:33:37 2024

@author: risha
"""

# def penalty(A,l):
#     c=0
#     for q in range(l-1):
#         if A[q]<A[q+1]:
#             c+=1
#     return c
for i in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    left = [0] * n
    right = [0] * n
    left[0] = 0
    for i in range(1, n):
        left[i] = left[i - 1] + (a[i] > a[i - 1])
    right[n - 1] = 0
    for i in range(n - 2, -1, -1):
        right[i] = right[i + 1] + (a[i] < a[i + 1])
    min_penalty = min(left[n - 1], right[0])
    for i in range(n - 1):
        min_penalty = min(min_penalty, left[i] + right[i + 1])
    print(min_penalty)
           