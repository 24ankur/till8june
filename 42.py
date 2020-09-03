N=int(input())
M=[]
for i in range(N):
    M.append(int(input()))

X=[]
for i in range(N):
    for j in range(i+1,N+1):
        a=M[i:j]

