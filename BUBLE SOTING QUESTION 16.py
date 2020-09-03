arr=[1,3,2,5,1,1,8,45,15,11,5,8]
n=len(arr)
c=0
for i in range(len(arr)):
    for j in range(len(arr)-1):
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]
            c=c+1
        else:
            pass



x=str(c)
print("Aray is sorted in",x+" swaps.")
print("FirstElement",arr[0])
print("LastElement",arr[n-1])
