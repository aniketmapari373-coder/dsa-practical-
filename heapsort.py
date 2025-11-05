class Heap:
    def __init__(self):
        self.arr = []
    def heapify(self, n, i):
        largest = i      # assume root is largest
        left = 2 * i + 1 # left child
        right = 2 * i + 2 # right child
        # If left child exists and is greater than root
        if left < n and self.arr[left] > self.arr[largest]:
            largest = left
        # If right child exists and is greater than largest so far
        if right < n and self.arr[right] > self.arr[largest]:
            largest = right
        # If largest is not root
        if largest != i:
            self.arr[i], self.arr[largest] = self.arr[largest], self.arr[i] # swap
            self.heapify(n, largest) # recursively heapify the affected subtree
    def build_max_heap(self):
        n = len(self.arr)
        # Start from last non-leaf node and move upwards
        for i in range(n // 2 - 1, -1, -1):
            self.heapify(n, i)
    def heapSort(self):
        n = len(self.arr)
        # Step 1: Build max heap
        self.build_max_heap()
        # Step 2: Extract elements one by one
        for i in range(n - 1, 0, -1):
            self.arr[0], self.arr[i] = self.arr[i], self.arr[0] # Swap root with last element
            self.heapify(i, 0) # Heapify reduced heap
    def display(self):
        for i in range(len(self.arr)):
            print(self.arr[i], end=' ')
        print()
# main function to execute heap sort
heap = Heap()
n = int(input("Enter number of elements: "))
print("Enter the elements:")
for _ in range(n):
    element = int(input())
    heap.arr.append(element)
print("Array before sorting:")
heap.display()
heap.heapSort()
print("Array after sorting:")
heap.display()
