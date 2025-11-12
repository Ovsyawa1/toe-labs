class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def __len__(self):
        length = 0
        current_node = self.head
        while (current_node):
            current_node = current_node.next
            length += 1

        return length

    def add_to_tail(self, new_value):
        self.size += 1
        new_node = Node(new_value)

        if self.head is None:
            self.head = new_node
            return 0

        last_node = self.head
        while (last_node.next):
            last_node = last_node.next
        last_node.next = new_node

    def add_to_head(self, new_value):
        self.size += 1
        new_node = Node(new_value)

        if self.head is None:
            self.head = new_node
            return 0

        new_node.next = self.head
        self.head = new_node

    def add_by_index(self, new_value, index: int):
        self.size += 1

        if (index < 0) or (index > self.size):
            self.size -= 1
            raise IndexError("List index out of range")
        elif index == 0:
            self.add_to_head(new_value)
            return 0
        elif index == self.size:
            self.add_to_tail(new_value)
            return 0

        previous_node = self.head
        for i in range(index - 1):
            previous_node = previous_node.next
        current_node = previous_node.next
        new_node = Node(new_value)
        new_node.next = current_node
        previous_node.next = new_node

    def del_head(self):
        if self.head is None:
            raise ValueError("Nothing to delete")

        self.size -= 1
        self.head = self.head.next

    def del_tail(self):
        if self.head is None:
            raise ValueError("Nothing to delete")

        previous_node = self.head
        current_node = previous_node.next

        if current_node is None:
            self.head = None
            return 0

        while current_node.next:
            previous_node = current_node
            current_node = current_node.next

        self.size -= 1
        previous_node.next = None

    def find_by_value(self, fvalue):
        current_node = self.head
        found_index = None
        index = 0

        while current_node is not None:
            if current_node.value == fvalue:
                found_index = index
            current_node = current_node.next
            index += 1

        return found_index

    def __str__(self):
        parts = []
        current = self.head
        while current is not None:
            parts.append(str(current.value))
            current = current.next
        return "[" + ", ".join(parts) + "]"

    def __getitem__(self, findex: int):
        if (findex >= 0) and (findex < self.size):
            current_node = self.head
            for i in range(findex):
                current_node = current_node.next
            return current_node.value
        else:
            raise IndexError("List index out of range")

    def __setitem__(self, findex: int, new_value):
        if (findex >= 0) and (findex < self.size):
            current_node = self.head
            for i in range(findex):
                current_node = current_node.next
            current_node.value = new_value
        else:
            raise IndexError("List index out of range")

    def __delitem__(self, index: int):
        if self.head is None:
            raise ValueError("Nothing to delete")

        if (index < 0) or (index >= self.size):
            self.size += 1
            raise IndexError("List index out of range")
        elif index == 0:
            self.del_head()
            return 0
        elif index == (self.size - 1):
            self.del_tail()
            return 0

        self.size -= 1
        previous_node = self.head
        for i in range(index - 1):
            if previous_node.next is None:
                break
            previous_node = previous_node.next
        current_node = previous_node.next
        previous_node.next = current_node.next
        current_node.next = None
