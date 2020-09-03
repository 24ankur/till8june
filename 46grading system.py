n=int(input())
for _ in range(n):
    grade=int(input())
    if grade<38:
        print(grade)

    else:

        for i in range(5):
            if (grade+i)%5==0 and i<3:
                print(grade+i)

            elif (grade+i)%5==0 and i>=3:
                print(grade)

