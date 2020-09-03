N,T = map(int, input().split())
w=[]
for _ in range(N):
    S=input().split()
    w.append(S)

w.sort(reverse=True,key=lambda i:i[1])
i=0
for j in range(T):
    print(w[j][i])
