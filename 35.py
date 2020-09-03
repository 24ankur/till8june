n=int(input())
arr=list(map(int,input().split()))
positive=0
negative=0
zero=0
for i in range(n):
    if arr[i] > 0:
        positive = positive + 1
    pos = (positive / n)

    if arr[i] < 0:
        negative = negative + 1

    neg = (negative / n)
    if arr[i]==0:


        zero = zero + 1

    z = (zero / n)

print("{:.6f}".format(pos))
print("{:.6f}".format(neg))
print("{:.6f}".format(z))
