l1=[]
arr=list(map(int,input().split()))
for i in range(1,max(arr)+1):
    l1.append(i)


for j in l1:
    if j in arr:
        pass
    else:
        print(j,end=" ")
