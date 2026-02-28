# Note: pop() on a stack makes .next start pointing back downwards. unlike appending where .next tends upwards to begin adding
class Node():
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack():
    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0

    def peek(self):
        return self.top

    def push(self, data):
        new_node = Node(data)
        if self.top == None:
            self.top = new_node
            self.bottom = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.length += 1

    def pop(self):
        if self.top == None:
            print("stack empty")
        else:
            self.top = self.top.next
            self.length-=1
            if (self.length == 0):
                self.bottom = None
            
    def print_stack(self):
        if self.top is None:
            print("Stack is empty")
        else:
            current_pointer = self.top
            while current_pointer is not None:
                print(current_pointer.data, end=" -> ")
                current_pointer = current_pointer.next
            print("None")


my_stack = Stack()

my_stack.peek()
my_stack.push("1st site: google.com")
my_stack.push("2nd site: udemy.com")
my_stack.push("3rd site: discord.com")
my_stack.peek()
my_stack.pop()
my_stack.print_stack()
