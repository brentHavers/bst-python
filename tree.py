from node import Node

class Tree:

    def __init__(self):
        self.root = None
        self.size = 0

    def insert(self, node: Node, value):
        if node is None:
            node = Node(value)
        else:
            if node.data > value:
                self.insert(node.right_child, value)
            else:
                self.insert(node.left_child, value)
        return