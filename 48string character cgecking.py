t = int(input())
for _ in range(t):
    s1 = input()
    s2 = input()
    for i in s1:
        if i in s2:
            print("Yes")
            break
    else:
        print("No")
