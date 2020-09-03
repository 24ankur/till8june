T=int(input())
for i in range(T):
    N,M,K=map(int,input().split())
    M1=[]
    M2=[]
    for j in range(N):
        NUM=list(map(int,input().split()))
        print(max(set(NUM),key=NUM.count),end=" ")