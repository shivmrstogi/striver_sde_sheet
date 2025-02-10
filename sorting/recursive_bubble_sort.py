arr = [13, 46, 24, 52, 20, 9]


def solve(arr, i, j):
    if i == j:
        return

    if arr[j + 1] < arr[j]:
        arr[j], arr[j + 1] = arr[j + 1], arr[j]

    solve(arr, i, j + 1)


def recursive_bubble_sort(arr, i):
    if i == 0:
        return

    solve(arr, i, 0)
    recursive_bubble_sort(arr, i - 1)


recursive_bubble_sort(arr, len(arr) - 1)
print(arr)
