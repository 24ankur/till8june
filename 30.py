s = input().strip()
n = int(input().strip())
L = len(s)
print(s.count('a') * (n//L) + s[:n % L].count('a'))