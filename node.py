class Node:
    left_child, right_child, data = None, None, None

    def __init__(self, key):
        self.left_child = None
        self.right_child = None
        self.data = key
