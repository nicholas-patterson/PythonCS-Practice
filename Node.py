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

