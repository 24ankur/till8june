n=int(input())
s = []
for i in range(n):
    x, y, a, b = input().split()
    if int(x)*int(y) == int(a) + int(b):
       s.append("Yes")
    else:
        s.append("No")
print('\n'.join(s))