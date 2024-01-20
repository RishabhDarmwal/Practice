# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 21:51:35 2024

@author: risha
"""

import sys
from typing import List
from functools import reduce

def function_to_sort(v: List[int]) -> List[int]:
    v.sort()
    return v

def main() -> None:
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        a.sort(reverse=True)
        b.sort()
        temp = []
        i, j = 0, n-1
        k, l = 0, m-1
        while i <= j:
            if abs(a[i] - b[k]) > abs(a[j] - b[l]):
                temp.append(abs(a[i] - b[k]))
                i += 1
                k += 1
            elif abs(a[i] - b[k]) < abs(a[j] - b[l]):
                temp.append(abs(a[j] - b[l]))
                l -= 1
                j -= 1
            else:
                temp.append(abs(a[j] - b[l]))
                if a[i] > b[i]:
                    l -= 1
                    j -= 1
                else:
                    i += 1
                    k += 1
        print(reduce(lambda x, y: x + y, temp, 0))

if __name__ == "__main__":
    main()
