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
            left_child_index = 2 * l
            right_child_index = left_child_index + 1
            if right_child_index < size and self.heap[right_child_index] < node and self.heap[right_child_index] < \
                    self.heap[left_child_index]:
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

    def update_value(self, old, new):
        old_index = self.rank[old]
        del self.rank[old]
        self.heap[old_index] = new
        self.rank[new] = old_index
        if old < new:
            self.down_heapify(old_index)
        else:
            self.up_heapify(old_index)


#  ----------------------------------------------Double Linked List--------------------------------------------------
class Node:
    # Node class for double linked list data structure

    def __init__(self, data):
        """
        Each node will be connected to other vertices with help of previous and next to complete double linked list
        :param data: value stored in node
        """
        self.prev = None
        self.data = data
        self.next = None


class DoubleLL:
    def __init__(self):
        "Each Dobule Linked list will have a head. If head is none then Linked List is empty"
        self.head = None

    def __len__(self) -> int:
        "Return length of double linked list"
        i = 0
        temp = self.head
        while temp is not None:
            temp = temp.next
            i += 1
        return i

    def is_empty(self) -> bool:
        """
        Check if Double linked list is empty or not
        :return: Boolean
        """
        return False if self.head else True

    def search(self, value) -> Node:
        """
        Search if given value exist as node in linked list
        :param value: data of node to find
        :return: Pointer to node with data = value
        """
        temp = self.head
        while temp is not None and temp.data != value:
            temp = temp.next
        return temp

    def prepend(self, new_node) -> None:
        """
        Insert new node in front of linked list
        :param new_node: New node to insert
        :return: None
        """
        new_node.next = self.head
        new_node.prev = None
        if self.head is not None:
            self.head.prev = new_node
        self.head = new_node


class Graph:
    def __init__(self):
        self.neighbor = []
        self.weight = []
        self.name2vertices = {}
        self.vertices2name = []

    def __len__(self) -> int:
        return len(self.vertices2name)

    def __getitem__(self, item):
        assert item in self.name2vertices, "Vertex must be part of Graph"
        return self.neighbor[self.name2vertices[item]]

    def add_vertex(self, data) -> str:
        assert data not in self.vertices2name
        self.name2vertices[data] = len(self.name2vertices)
        self.vertices2name.append(data)
        self.neighbor.append([])
        self.weight.append({})
        return f"{data} added to Graph"

    def add_arc(self, point_a, point_b, weight_ab=None):
        point_a = self.name2vertices[point_a]
        point_b = self.name2vertices[point_b]
        self.neighbor[point_a].append(point_b)
        self.weight[point_a][point_b] = weight_ab

    def add_edge(self, point_a, point_b, weight_ab=None):
        self.add_arc(point_a, point_b, weight_ab)
        self.add_arc(point_b, point_a, weight_ab)


# if __name__ == "__main__":
#     g = Graph()
#     g.add_vertex('a')
#     g.add_vertex('b')
#     g.add_vertex('c')
#     g.add_edge('a', 'b')
#     g.add_arc('a', 'c')
#     print(g.name2vertices)
#     print(g.neighbor)
#     print(g['d'])
