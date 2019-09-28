def shell_sort(arr):
    gap = len(arr)// 2

    while gap > 0:
        for i in range(gap, len(arr)):
            key = arr[i]
            j = i
            while j >= gap and arr[j - gap] > key:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = key
        gap //= 2


arr = [12, 34, 54, 2, 3]
shell_sort(arr)
for i in range(len(arr)):
    print(arr[i])