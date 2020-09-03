N = int(input())
M = []
sum=0
dum=0
for i in range(N):
    M.append(list(map(int,input().split())))

for i in range(N):
    for j in range(N):
        if i==j:
            sum=sum+M[i][j]

    dum=dum+M[i][N-1-i]

print(abs(dum-sum))

