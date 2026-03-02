class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        self.tail.next = new_node
        self.tail = new_node
        self.length += 1
        return self

    def prepend(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        self.length += 1
        return self

    def print_list(self):
        arr = []
        current_node = self.head
        while current_node is not None:
            arr.append(current_node.value)
            current_node = current_node.next
        print(arr)
        return arr

    def traverse_to_index(self, index):
        counter = 0
        current_node = self.head
        while counter != index:
            current_node = current_node.next
            counter += 1
        return current_node

    def insert(self, index, value):
        if index >= self.length:
            return self.append(value)
        if index == 0:
            return self.prepend(value)

        new_node = Node(value)
        leader = self.traverse_to_index(index - 1)
        holding_pointer = leader.next
        leader.next = new_node
        new_node.next = holding_pointer
        self.length += 1
        return self.print_list()

    def remove(self, index):
        if index == 0:
            self.head = self.head.next
            self.length -= 1
            return self.print_list()

        leader = self.traverse_to_index(index - 1)
        unwanted_node = leader.next
        leader.next = unwanted_node.next
        self.length -= 1
        return self.print_list()

    def reverse(self):
        if not self.head or not self.head.next:
            return self.head

        first = self.head
        second = first.next

        while second:
            temp = second.next  # saves value 16

            second.next = first  # 10 points to 1
            first = second
            second = temp

        self.head.next = None
        self.head = first  # The last node processed becomes the new head
        return self.print_list()


# Testing the implementation
my_linked_list = LinkedList(10)
my_linked_list.append(16)
my_linked_list.prepend(1)
# my_linked_list.insert(2, 99)
my_linked_list.insert(20, 88)

print("Before Reverse:")
my_linked_list.print_list()

print("After Reverse:")
my_linked_list.reverse()
