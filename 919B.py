# -*- coding: utf-8 -*-
"""
Created on Sat Jan 13 21:01:15 2024

@author: risha
"""

def solution():
    n, k, x = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    p_summ = [0] * n
    summ = 0
    for i in range(n):
        summ += a[i]
        p_summ[i] = summ
    ans = 0
    ri = n - 1
    li = ri - x + 1
    if li <= 0:
        ans = -1 * p_summ[ri]
    else:
        ans = 2 * p_summ[li - 1] - p_summ[ri]
    for i in range(max(n - k, 0), n):
        if i == 0:
            ans = max(ans, 0)
            continue
        ri = i - 1
        li = ri - x + 1
        if li <= 0:
            ans = max(ans, -1 * p_summ[ri])
        else:
            ans = max(ans, 2 * p_summ[li - 1] - p_summ[ri])
    print(ans)

t = int(input())
while t > 0:
    solution()
    t -= 1

