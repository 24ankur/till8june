N=int(input())
c=0
while N>0:
    if N%2==0:
        x=N/2
        N=x
        c=c+1

    else:
        N=N-1
        c=c+1
        if N==0:
            break

        else:
            x=N/2
            N=x
            c=c+1

print(c)