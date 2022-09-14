import os
os.system('cls||clear')

#----CODE STARTS HERE------

class FindPath:
    def __init__(self, root):
        self.root = root

    def insert(self, key):
        self.root = self.check_insertion(self.root, key)
      
    def check_insertion(self, node, element):
        if node == None:
            newNode = Node(element)
            return newNode
        elif node.data < element:
            newNode = self.check_insertion(node.right, element)
            node.right = newNode
        else:
            newNode = self.check_insertion(node.left, element)
            node.left = newNode
        return node

    def search(self, node, key):
        if node == None:
            return []
        elif node.data < key:
            traversedList = self.search(node.right, key)
            if len(traversedList) == 0:
                return []
            return [node.data] + traversedList
        elif node.data > key:
            traversedList = self.search(node.left, key)
            if len(traversedList) == 0:
                return []
            return [node.data] + traversedList
        else:
            return [node.data]


class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

root = Node(3)
tree = FindPath(root)
tree.insert(3)
tree.insert(5)
tree.insert(4)
tree.insert(2)
tree.insert(1)

print(tree.search(root, 4))