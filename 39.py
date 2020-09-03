T=int(input())
for i in range(T):
    M1=[]
    M2=[]
    N=int(input())
    arr=list(map(int,input().split()))
    for j in range(N):
        if arr[j]==1:
            M1.append(j)
    for k in range(len(M1)-1):
        M2.append(M1[k+1]-M1[k])

    for l in M2:
        if l<6:
            print("NO")
            break

    else:
        print("YES")
