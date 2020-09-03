from collections import deque

def array_left_rotation(a, n, k):
    a.rotate(-k)

n, k = map(int, input().strip().split(' '))
a = deque(map(int, input().strip().split(' ')))
array_left_rotation(a, n, k);
print(*a, sep=' ')