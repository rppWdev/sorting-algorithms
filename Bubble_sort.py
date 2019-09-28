def bubble_sort(arr):
    n = len(array)
    for i in range(n):
        for j in range(0, n - 1):
            if array[i] < array[j]:
                array[i], array[j] = array[j], array[i]


array = [2, 1, 5, 4, 3]
bubble_sort(array)
for i in range(len(array)):
    print(array[i])