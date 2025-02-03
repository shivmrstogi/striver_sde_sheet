arr =[13,46,24,52,20,9]

for i in range(1,len(arr)):
    j=i
    while j>=1 and arr[j]<arr[j-1]:
        tmp = arr[j]
        arr[j]=arr[j-1]
        arr[j-1]=tmp
        j-=1
print(arr)