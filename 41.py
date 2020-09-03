def P_factor(N,K):
    M1=[] #empty list for store primefactors
    factor=0
    i=2

    while i<=N/i:
        if N%i==0:
            factor=i
            M1.append(i)
            N=N/i
        else:
            i=i+1


    if factor<N:
        M1.append(N)

    else:
        M1.append(factor)


    if len(M1)<K:
        return 0
    else:
        return 1
T=int(input()) #testcases
for j in range(T):
    x1,x2=map(int,input().split())
    print(P_factor(x1,x2)) #function calling






