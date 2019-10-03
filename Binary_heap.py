class BinaryHeap:
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0

    def percUp(self, element):
        while element // 2 > 0:
            if self.heapList[element] < self.heapList[element // 2]:
                temp = self.heapList[element // 2]
                self.heapList[element // 2] = self.heapList[element]
                self.heapList[element] = temp
            element = element // 2

    def insert(self, element):
        self.heapList.append(element)
        self.currentSize = self.currentSize + 1
        self.percUp(self.currentSize)

    def percDown(self, element):
        while (element * 2) <= self.currentSize:
            min_child = self.minElement(element)
            if self.heapList[element] > self.heapList[min_child]:
                temp = self.heapList[element]
                self.heapList[element] = self.heapList[min_child]
                self.heapList[min_child] = temp
            element = min_child

    def minElement(self, element):
        if element * 2 + 1 > self.currentSize:
            return element * 2
        else:
            if self.heapList[element * 2] < self.heapList[element * 2 + 1]:
                return element * 2
            else:
                return element * 2 + 1

    def deleteMinElement(self):
        retval = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize = self.currentSize - 1
        self.heapList.pop()
        self.percDown(1)
        return retval

    def buildHeap(self, alist):
        elements = len(alist) // 2
        self.currentSize = len(alist)
        self.heapList = [0] + alist[:]
        while elements > 0:
            self.percDown(elements)
            elements = elements - 1

    def heapSort(self):
        for i in range(self.currentSize):
            print(self.deleteMinElement())

bh = BinaryHeap()
bh.buildHeap([0, 9, 5, 6, 2, 3, 11, 22, 2, 3, 5, 11, 6, 87, 41, 221, 421, 12])
bh.heapSort()




