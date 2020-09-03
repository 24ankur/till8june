k, n, w = map(int, input().split())
m = []
for i in range(1,w+1):
    m.append(i * k)

if n>=sum(m):
    print("0")

else:
    print(sum(m) - n)