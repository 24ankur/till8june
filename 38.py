def selling_car(T):
    for i in range(T):
        N=int(input())     #year
        P=list(map(int,input().split()))
        P=sorted(P,reverse=True)
        for j in range(N):
            P[j]=P[j]-j



        P = list(filter(lambda j: j > 0, P))
        print(sum(P) % 1000000007)







T=int(input()) #testcases
selling_car(T)