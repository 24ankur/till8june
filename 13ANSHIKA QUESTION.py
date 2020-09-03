i=0
l=list(map(int,input().split(",")))

l3=[]
x=[0,1,2,3]
for _ in x:
    l2 = []
    for j in range(len(l)):
        l2.append(l[j]+_)
    l3.append(l2)


print(l3)