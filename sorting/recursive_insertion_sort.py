arr = [13, 46, 24, 52, 20, 9]


def solve(arr, i):
    if i == 0:
        return

    if arr[i] < arr[i - 1]:
        arr[i], arr[i - 1] = arr[i - 1], arr[i]
        solve(arr, i - 1)
    else:
        return


def recursive_insertion_sort(arr, i):
    if i == len(arr):
        return

    solve(arr, i)
    recursive_insertion_sort(arr, i + 1)


recursive_insertion_sort(arr, 1)
print(arr)
