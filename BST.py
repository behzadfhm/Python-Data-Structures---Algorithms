from urllib.parse import non_hierarchical

from numpy import true_divide


class Node():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree():
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root == None:
            self.root = new_node
            return True
        temp = self.root
        while True:
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left == None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right == None:
                    temp.right = new_node
                    return True
                temp = temp.right
            if temp == None:
                temp = new_node

    def contains(self, value):
        temp = self.root
        while temp is not None:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
            return False


my_tree = BinarySearchTree()
my_tree.insert(4)
print(my_tree.root.value)
my_tree.insert(3)
print(my_tree.root.left.value)
print(my_tree.contains(5))
