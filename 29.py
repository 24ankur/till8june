N=int(input())
l1=list(map(int,input().split()))


Q=int(input())
for i in range(Q):
    y,x=map(int,input().split())
    if y==0:
        C = 0

        for j in l1:
            if j>=x:
                C=C+1

        print(C)

    else:
        R = 0
        for j in l1:
            if j>x:
                R=R+1

        print(R)

