n,m,g=map(int,input().split())

time=list(map(int,input().split()))

arr=list(map(int,input().split()))
D_time=[]
c=0
for i in range(m-1):
    R_time=time[i+1]-time[i]
    D_time.append(R_time)


for x in range(g):

    for q in arr:

        if D_time[x]>=q:
            c=c+1
            break

print(c)
