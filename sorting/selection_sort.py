arr = [4, 1, 3, 9, 7]

for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if arr[j]<arr[i]:
            tmp = arr[i]
            arr[i]=arr[j]
            arr[j]= tmp

print(arr)