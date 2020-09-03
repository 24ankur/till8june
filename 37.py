N,Q=map(int,input().split())
arr=list(map(int,input().split()))

x=list(map(int,input().split()))
for i in x:
    c=0
    for j in range(N):
        c=c+arr[j]
        if c>=i:
            print(j+1)

            break



