# -*- coding: utf-8 -*-
"""
Created on Sat Jan 13 20:44:17 2024

@author: risha
"""

for t in range(int(input())):
    n = int(input())
    a = []
    b = []
    for i in range(n):
        a_i, b_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)
    ex = []
    mx = float('-inf')
    mn = float('inf')
    found = False
    for i in range(n):
        if a[i] == 1:
            mx = max(mx, b[i])
        if a[i] == 2:
            mn = min(mn, b[i])
        else:
            if a[i] == 3:
                ex.append(b[i])
    if mx > mn:
        print(0)
        continue
    s = set()
    ans = 0
    while len(ex) != 0:
        ele = ex.pop()
        if ele >= mx and ele <= mn:
            s.add(ele)
    print(mn - mx + 1 - len(s))

