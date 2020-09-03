#!/bin/python3

from collections import Counter, defaultdict, deque
from sys import exit, stderr

def read(f): return map(f, input().split())
def readlist(f): return [f(x) for x in input().split()]

M = 10**9 + 7
N, Q = read(int)
S = [ord(c) - ord('a') for c in input().strip()]

def combs(d):
    if not d:
        return 0
    c, n = d.popitem()
    s = 2 ** n - 1
    r = 2 ** (n - 1) * combs(d)
    return (s + r) % M

for q in range(Q):
    query = readlist(int)
    if query[0] == 1:
        i, j, t = query[1:]
        if t % 26:
            for k in range(i, j + 1):
                S[k] = (S[k] + t) % 26
    elif query[0] == 2:
        i, j = query[1:]
        d = Counter(S[i:j+1])
        print(combs(d))