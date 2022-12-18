class MyHeap:
    def __init__(self, nodes):
        self.heap = [None]
        self.rank = {}
        for node in nodes:
            self.push(node)

    def __len__(self):
        return len(self.heap) - 1

    def push(self, node):
        assert node not in self.rank
        l = len(self.heap)

        self.heap.append(node)
        self.rank[node] = l
        self.up_heapify(l)

    def up_heapify(self, l):
        node = self.heap[l]
        while l > 1 and node < self.heap[l // 2]:
            self.heap[l] = self.heap[l // 2]
            self.rank[self.heap[l // 2]] = l
            l //= 2
        self.heap[l] = node
        self.rank[node] = l

    def pop(self):
        root = self.heap[1]
        del self.rank[root]

        # Replace root with last leaf of heap
        node = self.heap.pop()
        if self:
            self.heap[1] = node
            self.rank[node] = 1
            self.down_heapify(1)
        return root

    def down_heapify(self, l):
        node = self.heap[l]
        size = len(self.heap)
        while True:
            left_child_index = 2*l
            right_child_index = left_child_index + 1
            if right_child_index < size and self.heap[right_child_index]<node and self.heap[right_child_index]<self.heap[left_child_index]:
                self.heap[l] = self.heap[right_child_index]
                self.rank[self.heap[right_child_index]] = l
                l = right_child_index
            elif left_child_index < size and self.heap[left_child_index] < node:
                self.heap[l] = self.heap[left_child_index]
                self.rank[self.heap[left_child_index]] = l
                l = left_child_index
            else:
                self.heap[l] = node
                self.rank[node] = l
                return
