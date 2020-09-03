s=list(map(int,input().split()))
l1=[]
l3=[]
l2=["a","e","i","o","u"]
for i in range(len(s)):
    for j in range(i+1,len(s)+1):
        l1.append(s[i:j])

print(l1)