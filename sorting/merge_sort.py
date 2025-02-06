arr = [10, 1, 3, 6]


def merge(a, b):
    merged_arr = []
    i = 0
    j = 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            merged_arr.append(a[i])
            i += 1
        else:
            merged_arr.append(b[j])
            j += 1
    while i < len(a):
        merged_arr.append(a[i])
        i += 1
    while j < len(b):
        merged_arr.append(b[j])
        j += 1

    return merged_arr


def merge_sort(arr):
    if len(arr) == 1 or len(arr) == 0:
        return arr

    i = 0
    j = len(arr) - 1
    mid = (i + j) // 2

    first_sorted = merge_sort(arr[i : mid + 1])
    second_sorted = merge_sort(arr[mid + 1 : j + 1])

    sorted_array = merge(first_sorted, second_sorted)

    return sorted_array


print(merge_sort(arr))
