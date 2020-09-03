n = int(input())
arr = list(map(int, input().split()))
y=set(arr)
c=0
r=[]
for j in y:
    c=0
    for i in arr:
        if j==i:
            c=c+1

    r.append(c//2)

print(sum(r))


