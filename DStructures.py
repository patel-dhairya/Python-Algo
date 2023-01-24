class Stack:
    """Stack data structure implementation using List """

    def __init__(self):
        """
        Initialise empty stack
        """
        self._stack = []

    def __len__(self) -> int:
        """
        Return number of elements in stack
        """
        return len(self._stack)

    def is_empty(self):
        """
        Check if stack is empty
        """
        return len(self._stack) == 0

    def push(self, e):
        """
        Add element e to top of stack/end of list
        """
        self._stack.append(e)

    def top(self):
        """
        Return top element of the stack
        """
        assert self.is_empty() is False, "Cannot get top element of empty stack"
        return self._stack[-1]

    def pop(self):
        """
        Remove the top element of the stack
        :return: Top element of stack
        """
        assert self.is_empty() is False, "Cannot remove element from empty stack"
        return self._stack.pop()


class Queue:
    """ FIFO data structure Queue implemented with circular list """
    _DEFAULT = 8  # initial capacity of new queue

    def __init__(self):
        """
        Initialise empty queue
        """
        self._queue = [None] * Queue._DEFAULT
        self._length = 0  # Size of queue
        self._front_start = 0  # Index referencing to front element of queue

    def __len__(self) -> int:
        """
        Returns number of elements in queue
        """
        return self._length

    def is_empty(self) -> bool:
        """
        Check if queue is empty
        """
        return self._length == 0

    def first(self):
        """
        Return front element of queue if it exists else raise error
        """
        assert self.is_empty() is False, "Cannot get front element of empty queue"
        return self._queue[self._front_start]

    def _change_size(self, new_length: int) -> None:
        """
        Create a new queue with given new length
        :param new_length: New size of list for queue
        :return: None
        """
        old_queue = self._queue
        self._queue = [None] * new_length
        start = self._front_start

        for i in range(self._length):
            self._queue[i] = old_queue[start]
            start = (start + 1) % len(old_queue)
        self._front_start = 0

    def dequeue(self):
        """
        Remove and return front element of queue if it exists else raise error
        """
        assert self.is_empty() is False, "Cannot remove front element of empty queue"
        answer = self._queue[self._front_start]
        self._queue[self._front_start] = None
        self._front_start = (self._front_start + 1) % len(
            self._queue)  # Modulo helps with circular array index
        self._length -= 1

        # If number of elements in queue are less than 4th of current array size used by queue,
        # reduce array to half of its current size
        if len(self._queue) // 4 > self._length > 0:
            self._change_size(len(self._queue) // 2)

        return answer

    def enqueue(self, e):
        """
        Add element e to back of queue
        """
        if len(self._queue) == self._length:
            self._change_size(len(self._queue) * 2)
        current_empty_index = (self._front_start + self._length) % len(self._queue)
        self._queue[current_empty_index] = e
        self._length += 1


class BST:
    """
    Binary search tree is a tree where each node has up to two children.
    Addition condition is that values in left subtree of node are always less than value of that
    node of tree and values in right subtree of node are always greater than value of that node.
    Left and right subtrees of node are also always binary tree
    """

    class __Node:
        """
        Node class represent node of binary search tree.
        """

        def __init__(self, data, left=None, right=None):
            self._data = data
            self._left = left
            self._right = right

        def get_data(self):
            return self._data

        def get_left(self):
            return self._left

        def get_right(self):
            return self._right

        def set_data(self, data):
            self._data = data

        def set_left(self, left_node):
            self._left = left_node

        def set_right(self, right_node):
            self._right = right_node

        def __iter__(self):
            """
            Iterate values with ascending order
            """
            if self._left is not None:
                for node in self._left:
                    yield node

            yield self._data

            if self._right is not None:
                for node in self._right:
                    yield node

    def __init__(self):
        self._root = None

    def add(self, data):
        """
        Create a node with given data and add it to appropriate location in Binary search tree
        """

        def __add(root: BST.__Node, new_data) -> BST.__Node:
            if root is None:
                return BST.__Node(new_data)
            if root.get_data() > new_data:
                root.set_left(__add(root.get_left(), new_data))
            else:
                root.set_right(__add(root.get_right(), new_data))
            return root

        self._root = __add(self._root, data)

    def __iter__(self):
        if self._root is not None:
            return self._root.__iter__()
        return [].__iter__()


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
            if right_child_index < size and self.heap[right_child_index] < node and self.heap[
                right_child_index] < \
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


#  -Double Linked List-
class Node:
    # Node class for double linked list data structure

    def __init__(self, data):
        """
        Each node will be connected to other vertices with help of previous and next to complete
        double linked list
        :param data: value stored in node
        """
        self.prev = None
        self.data = data
        self.next = None


class DoubleLL:
    def __init__(self):
        """Each Double Linked list will have a head. If head is none then Linked List is empty"""
        self.head = None

    def __len__(self) -> int:
        """Return length of double linked list"""
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


def main():
    pass

# if __name__ == "__main__":
#     main()
