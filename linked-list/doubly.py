# My Explanation:
# new_node is 7. this is the new node we want to insert between 5 and 16

# separately we state, the current node is our head node, which is 4

# we loop range once, and this once range loop allows our current node to go from 4 to 5. 
# so the new current node at this point is 5.  via current_node = current_node.next

# then, the previous pointer on our new_node which is 7, is now aware of the current_node which is 5. 
# creating a bi-directional relationship. 
# the next pointer on the new_node, which is 7 is now pointing to the current_node.next, which is 16. 
# because after 7 is 16 in the list. 

# then current_node.next which is the next pointer on 5, has awareness on 7, which is the new_node

# now finally, the next pointer on new node, which new_node.next points to 16, we say 16 has a previous pointer pointing back 7

# then we increase length of the linked list. 

class Node():
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None


class DoublyLinkedList():
    def __init__(self):
        self.head = None
        self.tail = self.head
        self.length = 0

    def print_list(self):
        if self.head == None:
            print("Empty")
        else:
            current_node = self.head
            while current_node!= None:
                print(current_node.data, end= ' ')
                current_node = current_node.next
        print()

    def append(self, data):
        new_node = Node(data)
        if self.head == None: #If linked list is empty, we make head and tail both equal to the new node
            self.head = new_node
            self.tail = self.head
            self.length += 1
            return
        else: #Else, we make the previous pointer of the new node point to the present tail.
            new_node.previous = self.tail
            self.tail.next = new_node #Then we make the next pointer of the present tail point to the new node thus establishing a two way link between the present tail and the new node
            self.tail = new_node #Finally we update the tail to be equal to the new node
            self.length += 1
            return

    def prepend(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            self.tail = self.head
            self.length += 1
            return
        else:
            new_node.next = self.head #We make the next of the new node point to the present head
            self.head.previous = new_node #We establish a two-way link by making the previous of the present head point to the new node
            self.head = new_node #Finally we update the head
            self.length += 1
            return

    def insert(self, position, data):
        if position == 0:
            self.prepend(data) #Inserting at position 0 is equivalent to prepending. So instead of repeating code, we simple call the prepend method
            return
        if position >= self.length:
            if position > self.length:
                print('This position is not available. Inserting at the end of the list')
            self.append(data) #Similarly, inserting ata position >= the length of the list is equivalent to appending, so we call the append method
            return
        else:
            new_node = Node(data)

            current_node = self.head

            for i in range(position - 1): #We traverse upto one position before the position where we want to insert the new node
                current_node = current_node.next
            
            new_node.previous = current_node # 5
            new_node.next = current_node.next #And the next point to the next of the current node.
            current_node.next = new_node #Then we break the link between the current node and the next node and make the next of the current node point to the new node
            new_node.next.previous = new_node #And finally we update the previous of the next node to point to the new node instead of the current node. This way, the new node gets inserted in betwwen the current and the next nodes.
            self.length += 1
            return

    def delete_by_value(self, data):
        if self.head == None:
            print("Linked List is empty. Nothing to delete.")
            return

        current_node = self.head
        if current_node.data == data:
            self.head = self.head.next
            if self.head == None or self.head.next==None: #If after deleting the first node the list becomes empty or there remains only one node, we set the tail equal to the head
                self.tail = self.head
            if self.head != None:
                self.head.previous = None #We set the previous pointer of the new head to be None
            self.length -= 1
            return
        try:  # Try block required as if the value is not found then current_node.next will be None and there is no data parameter to compare.
            while current_node!= None and current_node.next.data != data:
                current_node = current_node.next
            if current_node!=None:
                current_node.next = current_node.next.next
                if current_node.next != None: #If the node deleted is not the last node(i.e., the node next to the next to the current node is !- None),
                    current_node.next.previous = current_node #Then we set the previous of the node next to the deleted node equal to the current node, so a two-way link is established
                else:
                    self.tail = current_node #If the deleted node is the last node then we update the tail to be the current node
                self.length -= 1
                return
        except AttributeError:
            print("Given value not found.")
            return

    def delete_by_position(self, position):
        if self.head == None:
            print("Linked List is empty. Nothing to delete.")
            return

        if position == 0:
            self.head = self.head.next
            #print(self.head)
            if self.head == None or self.head.next == None:
                self.tail = self.head
            if self.head != None:
                self.head.previous = None #We update the previous of the new head to be equal to None
            self.length -= 1
            return

        if position>=self.length:
            position = self.length-1

        current_node = self.head
        for i in range(position - 1):
            current_node = current_node.next
        current_node.next = current_node.next.next
        if current_node.next != None: #Similar logic to the delete_by_value method
            current_node.next.previous = current_node
        else:
            self.tail = current_node
        self.length -= 1
        return


my_linked_list = DoublyLinkedList()
# my_linked_list.print_list()
#Empty

my_linked_list.append(5)
my_linked_list.append(16)

# my_linked_list.print_list()
#5 2 9

my_linked_list.prepend(4)
my_linked_list.print_list()
# #4 5 2 9

my_linked_list.insert(2,7)
my_linked_list.print_list()
# # #4 5 7 2 9

# my_linked_list.insert(0,0)
# my_linked_list.insert(6,0)
# my_linked_list.insert(9,3)
# my_linked_list.print_list()
# #This position is not available. Inserting at the end of the list
# #0 4 5 7 2 9 0 3

my_linked_list.delete_by_value(3)
my_linked_list.print_list()
# #0 4 5 7 2 9 0

# my_linked_list.delete_by_value(0)
# my_linked_list.print_list()
# #4 5 7 2 9 0

# my_linked_list.delete_by_position(3)
# my_linked_list.print_list()
# #4 5 7 9 0

# my_linked_list.delete_by_position(0)
# my_linked_list.print_list()
# #5 7 9 0

# my_linked_list.delete_by_position(8)
# my_linked_list.print_list()
# #5 7 9

# my_linked_list.delete_by_value(3)
# my_linked_list.print_list()
# #Given value not found.

# print(my_linked_list.length)
#3


#The answers are all same. Meaning our doubly linked list works properly
