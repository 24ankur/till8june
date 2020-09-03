x=input()
c=0
r=0
ch="z"
for i in x:
    if i==ch:
        c=c+1

    else:
        r=r+1


if 2*c==r:
    print("Yes")

else:
    print("No")
