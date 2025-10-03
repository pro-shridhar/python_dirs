class MaxHeap:

    def __init__(self):
        self.heap = []

    def add(self, data):
        self.heap.append(data)
        self.heap_up(len(self.heap) - 1)

    def heap_up(self, index):

        prent_index = (index - 1) // 2

        if index > 0 and self.heap[index] > self.heap[prent_index]:
            self.heap[index], self.heap[prent_index] = (
                self.heap[prent_index],
                self.heap[index],
            )
            self.heap_up(prent_index)

    def get_max(self):
        if not self.heap:
            return None
        return self.heap[0]

    def extrect_max(self):
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        max_val = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.heap_down(0)

        return max_val

    def heap_down(self, index):
        largest = index
        left = 2 * index + 1
        right = 2 * index + 2
        size = len(self.heap) - 1

        if left < size and self.heap[left] > self.heap[largest]:
            largest = left
        if right < size and self.heap[right] > self.heap[largest]:
            largest = right

        if largest != index:
            self.heap[largest], self.heap[index] = self.heap[index], self.heap[largest]
            self.heap_down(largest)

    def print_heap(self):
        print(self.heap)


maxh = MaxHeap()
maxh.add(12)
maxh.add(1)
maxh.add(32)
maxh.add(15)
maxh.add(10)
maxh.add(9)
maxh.print_heap()
print(maxh.extrect_max())
maxh.print_heap()
print(maxh.extrect_max())
maxh.print_heap()
