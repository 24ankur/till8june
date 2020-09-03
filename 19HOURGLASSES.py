M = []
for _ in range(6):
    M.append(list(map(int, input().split())))

mask = ((0,0), (0,1), (0, 2), (1,1), (2, 0), (2, 1), (2, 2))

T = -63

for r in range(4):
    for c in range(4):
        C=0

        for m in mask:
            C += M[m[0]+r][m[1]+c]
        T = max(T, C)

print(T)