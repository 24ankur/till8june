t=int(input())
for i in range(0, t):
    M = input().split()

    m = int(M[0])
    n = int(M[1])

    if len(str(m + n)) == len(str(n)):
        print(n)
    else:
        print(m + n)