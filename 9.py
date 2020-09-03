def number_in(l1,N,num):
    for i in l1:
        for j in l1:
            if i+j==num:
                return True











l1=[1,2,3,4,5,6]
num=19
N=len(l1)
if (number_in(l1,N,num)==True):
    print("found")
else:
    print("not found")
