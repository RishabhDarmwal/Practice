# -*- coding: utf-8 -*-
"""
Created on Sat Jan 13 21:50:42 2024

@author: risha
"""

import math
from collections import defaultdict

divs = []

def findDiv(n):
    global divs
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            if n // i == i:
                divs.append(i)
            else:
                divs.append(i)
                divs.append(n // i)

def solve():
    n = int(input())
    ar = list(map(int, input().split()))
    divs.clear()
    findDiv(n)
    ans = 1
    for i in range(len(divs)):
        if divs[i] == n:
            continue
        mp = defaultdict(list)
        for j in range(1, n + 1):
            mp[j % divs[i]].append(ar[j - 1])
        var = 0
        for x in mp.values():
            pp = 0
            x.sort()
            for i in range(1, len(x)):
                pp = math.gcd(pp, x[i] - x[i - 1])
            var = math.gcd(var, pp)
        if var != 1:
            ans += 1
    print(ans)

t = int(input())
for _ in range(t):
    solve()

