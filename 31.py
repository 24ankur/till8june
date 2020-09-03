N=int(input())
s=input()
c=0
curent=0
for i in s:
    if i=="D" and curent==0:
        c=c+1

    if i=="U":
        curent=curent+1

    else:
        curent=curent-1


print(c)

