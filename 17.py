s=input()
c=0
res=0
l1=['a','e','i','o','u']
for i in range(len(s)):
    if s[i] in l1:
        c=c+1
        res=max(res,c)

    else:
        c=0


print(res)