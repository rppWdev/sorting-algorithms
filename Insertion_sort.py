import time
import random

def insertion_sort(arr):
    start_time = time.time()
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

    print("Sorted array is:  %f s" %((time.time() - start_time)))
    for i in range(len(arr)):
        print("%d" % arr[i])


arr = [12, 11, 13, 5, 6]
insertion_sort(arr)
