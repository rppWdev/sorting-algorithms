def quick_sort(alist, start, end):
    if end - start > 1:
        p = partition(alist, start, end)
        quick_sort(alist, start, p)
        quick_sort(alist, p+1, end)


def partition(alist, start, end):
    pivot = alist[start]
    i = start + 1
    j = end - 1

    while True:
        while i <= j and alist[i] <= pivot:
            i += 1
        while i <= j and alist[j] >= pivot:
            j = j - 1

        if i <= j:
            alist[i], alist[j] = alist[j], alist[i]
        else:
            alist[start], alist[j] = alist[j], alist[start]
            return j


alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
quick_sort(alist, 0, len(alist))
print(alist)