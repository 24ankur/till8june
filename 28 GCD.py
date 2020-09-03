a,b,c=map(int,input().split())
l1=[a,b,c]
l2=[]
y=max(l1)
print(y)
for i in range(1,y):
    if a%i==0 and b%i==0 and c%i==0:
        l2.append(i)


print(max(l2))


