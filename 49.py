def BennyAndGift(DR):
    D = {}
    current = (0, 0)
    D[current] = None
    fall = 0
    for d in DR:40
        if d == "L":
            current = (current[0] - 1, current[1])
        elif d == "R":
            current = (current[0] + 1, current[1])
        elif d == "U":
            current = (current[0], current[1] - 1)
        elif d == "D":
            current = (current[0], current[1] + 1)
        # print(current)

        if current in D:
            fall += 1
        else:
            D[current] = None
    return fall


print(BennyAndGift(input()))