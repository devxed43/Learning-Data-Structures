# === my conceptual understanding of singly linked lists:===
# tail does not belong to any node. tail is a representation on an entire linked list to represent which node has been created as of latest?
# essentially next belongs to nodes and a tail belongs to an entire linked list

class Node():
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = self.head
        self.length = 0

    def append(self, data):
        # create new node with data
        new_node = Node(data)

        # linked lists head
        if self.head == None:
            self.head = new_node
            self.tail = self.head  # self.tail of linked list points at latest created node
            self.length = 1  # length is now 1
        else:
            # if not starting at the head, and there's already a node after the head
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1

    # has own scope
    # in else block
    # new node created's next pointer, points to self.head
    # the order its coded in, symbolizes its created before it
    # so it can point its next to the head
    # the tail of the newly created node is the self.head
    # we increment length
    def prepend(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            self.tail = self.head
            self.length += 1
        else:
            new_node.next = self.head
            self.head = new_node
            self.length += 1

    def print_list(self):
        if self.head == None:
            print("empty")
            return True
        else:
            current_node = self.head
            while current_node != None:
                print(current_node.data, end="-->")
                current_node = current_node.next
        print()

    # super tedious. since LL's are not index based, we have to manually move the data through the nodes to the next nodes
    def insert(self, position, data):
        print('items:', self.length)
        print('insert at index:', position)

        if position >= self.length:
            if position > self.length:
                print("inserting at the end of LL")
            # create a new node to insert into LL chain
            new_node = Node(data)

            self.tail.next = new_node
            self.tail = new_node
            self.length += 1

        # if the index we want to insert at is beginning
        elif position == 0:

            # create new node
            new_node = Node(data)

            # the next pointer of this new node points to the head
            # the position in which this is coded signifies its the new beginning
            new_node.next = self.head

            # now, the new head of the LL is the new node we created
            self.head = new_node

            # simply up the length
            self.length += 1
        else:
            # create the new node of 🚀
            new_node = Node(data)

            # current node to begin looping from
            current_node = self.head  # 222

            # we target the index before the position we want to insert at
            for i in range(position-1):
                # this is how we loop from node to node
                # the next element after current becomes new current
                # rightward movement
                current_node = current_node.next

            # position index 3, jumps to position index 4
            # 🚀.next jumps to next node after it
            # our node at position 3, is now shifted over to the space after it (position 4)
            new_node.next = current_node.next

            # position index 4 is now our newly created node
            # the position 4 is now our new node rocket ship
            current_node.next = new_node

            # result
            # [222] -> [17] -> [13] -> [23] -> [🚀] -> [70] -> [3] -> [5] -> [2] -> None

            self.length += 1

    def delete_by_value(self, data):
        if self.head == None:
            print("Linked List is empty. Nothing to delete.")
            return
        current_node = self.head

        if current_node.data == data:
            self.head = self.head.next
            if self.head == None or self.head.next == None:
                self.tail = self.head
            self.length -= 1
            return

        while current_node.next != None and current_node.next.data != data:
            # if current_node.data == data:
            #    previous_node.next = current_node.next
            #    return
            current_node = current_node.next
        if current_node.next != None:
            current_node.next = current_node.next.next

            if current_node.next == None:
                self.tail = current_node
            self.length -= 1
            return
        else:
            print("Given value not found.")

    def delete_by_position(self, position):
        
        if self.head == None:
            print("Linked List is empty. Nothing to delete.")
            return
        
        if position == 0:
            self.head = self.head.next
            if self.head == None or self.head.next == None:
                self.tail = self.head
            self.length -= 1
            return
        
        if position >= self.length:
            position = self.length-1
        
        current_node = self.head

        for i in range(position - 1):
            current_node = current_node.next
        current_node.next = current_node.next.next
        self.length -= 1
        if current_node.next == None:
            self.tail = current_node
        return


if __name__ == '__main__':
    my_linked_list = LinkedList()

    my_linked_list.append(5)
    my_linked_list.append(2)
    my_linked_list.prepend(3)
    my_linked_list.prepend(70)
    my_linked_list.prepend(23)
    my_linked_list.prepend(13)
    my_linked_list.prepend(17)
    my_linked_list.prepend(222)

    my_linked_list.insert(4, '🚀')  # insert

    # delete a specific item
    # my_linked_list.print_list()
    # my_linked_list.delete_by_value(222)
    # my_linked_list.print_list()

    # my_linked_list.delete_by_position(3)
    my_linked_list.print_list()
    my_linked_list.delete_by_position(3)
    my_linked_list.print_list()

    # my_linked_list.print_list()

    # my_linked_list.delete_by_value(0)
    # my_linked_list.print_list()

    # my_linked_list.delete_by_position(3)
    # my_linked_list.print_list()

    # my_linked_list.delete_by_position(0)
    # my_linked_list.print_list()

    # my_linked_list.delete_by_position(8)
    # my_linked_list.print_list()

    # print(my_linked_list.length)
