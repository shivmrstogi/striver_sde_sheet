arr =[13,46,24,52,20,9]

for i in range(len(arr)-1,-1,-1):
    for j in range(0,i):
        if arr[j]>arr[j+1]:
            tmp = arr[j]
            arr[j]=arr[j+1]
            arr[j+1]=tmp
print(arr)