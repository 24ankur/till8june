L1=[]
arr=list(map(int,input().split()))
for j in range(1,10+1):
    L1.append(j)

s1=set(L1)
s2=set(arr)

result=s1.symmetric_difference(s2)
print(result)



