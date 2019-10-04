def heapify(arr, size, element):
    largest = element
    left = 2 * element + 1
    right = 2 * element + 2

    if left < size and arr[element] < arr[left]:
        largest = left

    if right < size and arr[largest] < arr[right]:
        largest = right

    if largest != element:
        arr[element], arr[largest] = arr[largest], arr[element]

        heapify(arr, size, largest)

def heap_sort(arr):
    size = len(arr)

    for i in range(size - 1, -1, -1):
        heapify(arr, size, i)

    for j in range(size - 1, 0, -1):
        arr[j], arr[0] = arr[0], arr[j]
        heapify(arr, j, 0)


arr = [12, 11, 13, 5, 6, 7]
heap_sort(arr)
n = len(arr)
print ("Sorted array is")
for i in range(n):
    print ("%d" %arr[i])


