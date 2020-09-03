def first(e):
    return e[0]

N=int(input())
l1=[]
l2=[]
l3=[]
for i in range(N):
    x=input().split()
    l1.append(x[0])
    l2.append(int(x[1]))


d=list(zip(l2,l1))
d.sort(reverse=True,key=first)
for i in d:
    l3.append(i[1])

print(l3[0])