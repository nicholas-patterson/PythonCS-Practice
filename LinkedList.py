class Node:
    def __init__(self, data, next_node=None):
        self.next_node = next_node
        self.data = data

    def get_value(self):
        return self.data

    def get_next_node(self):
        return self.next_node

    def set_next_node(self, next_node):
        self.next_node = next_node


class LinkedList:
    def __init__(self, head_node=None):
        self.head_node = head_node

    def get_head_node(self):
        return self.head_node

    def insert_beginning(self, new_value):
        new_node = Node(new_value)
        new_node.set_next_node(self.head_node)
        self.head_node = new_node

    def insert_end(self, new_value):
        new_node = Node(new_value)
        current_node = self.head_node
        if self.head_node is None:
            self.head_node = new_node

        while current_node.get_next_node() is not None:
            current_node = current_node.get_next_node()
        current_node.set_next_node(new_node)

    def remove_node(self, value_to_remove):
        current_node = self.head_node
        while current_node:
            if current_node.get_value() == value_to_remove:  # checking if item to remove is in the head
                self.head_node = current_node.get_next_node()
            else:
                while current_node:
                    after_head = current_node.get_next_node()
                    if after_head.get_value() == value_to_remove:
                        current_node.set_next_node(after_head.get_next_node())
                        current_node = None
                    else:
                        current_node = after_head

    def print_list(self):
        string_list = ""
        current_node = self.head_node
        while current_node:
            if current_node.get_value() is not None:
                string_list += str(current_node.get_value()) + "\n"
            current_node = current_node.get_next_node()
        return string_list


# Creating Nodes
my_node_1 = Node(100)
my_node_2 = Node(200)
my_node_3 = Node(300)
my_node_4 = Node(400)

# Adding Nodes To List
my_linked_list = LinkedList(my_node_1)
my_linked_list.insert_end(my_node_2.get_value())
my_linked_list.insert_end(my_node_3.get_value())
my_linked_list.insert_end(my_node_4.get_value())


print(my_linked_list.print_list())
