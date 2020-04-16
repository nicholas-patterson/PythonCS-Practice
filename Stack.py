from Node import Node


class Stack:
    def __init__(self, limit=5):
        self.first_item = None
        self.limit = limit
        self.size = 0

    def push(self, value):
        if self.limit > self.size:
            new_item = Node(value)
            new_item.set_next_node(self.first_item)
            self.first_item = new_item
            self.size += 1
        else:
            print(f"The stack is full it has: {self.size} items, try removing one first")

    def pop(self):
        if self.size > 0:
            item_to_pop = self.first_item
            self.first_item = item_to_pop.get_next_node()
            self.size -= 1
            return item_to_pop.get_value()
        else:
            print("Cannot remove item, List is empty")

    def peek(self):
        if self.size > 0:
            return self.first_item.get_value()
        else:
            print("Cannot peak nothing in list")

    def print_stack(self):
        stringy_stack = ""
        while self.first_item:
            if self.first_item.get_value() is not None:
                stringy_stack += str(self.first_item.get_value()) + "\n"
            self.first_item = self.first_item.get_next_node()
        return stringy_stack


# Making my node
my_node_1 = Node(10)
my_node_2 = Node(20)
my_node_3 = Node(30)
my_node_4 = Node(40)
my_node_5 = Node(50)
my_node_6 = Node(60)


# Making new stack
my_stack = Stack()

# Pushing to Stack

my_stack.push(my_node_1.get_value())
my_stack.push(my_node_2.get_value())
my_stack.push(my_node_3.get_value())
my_stack.push(my_node_4.get_value())
my_stack.push(my_node_5.get_value())
# my_stack.push(my_node_6.get_value()) # Will not add to stack because limit is 5


# Print Stack
print(my_stack.print_stack())

