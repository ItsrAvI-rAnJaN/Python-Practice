# pseduo Code

"""
class Bst:
    __init__():
     data
     left_child
     right_child

class BinarySearchTree:
    __init__():
       root : Int

    _insert(data,current_node):
       make  for inserting data in Tree

    insert(data):
        _insert(data,current_node)
    
    _search(value,current_node):
        for searching node

    search(value):
        _search(value,Current_)

    _inorder_transversal(current_node):
        first left transversal
        current_node transversal
        at last right transversal
    inorder_transversal():
        _inorder_transversal()
"""


class Bst:
        def __init__(self, data:Int):
            self.data = data
            self.leftChild = None
            self.rightChild = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def _insert(self, data, current_node):
        if data < current_node.data:
            if not current_node.leftChild:
                current_node.leftChild = Bst(data)
            else:
                self._insert(data, current_node.leftChild)
        elif data > current_node.data:
            if not current_node.rightChild:
                current_node.rightChild = Bst(data)
            else:
                self._insert(data, current_node.rightChild)

    def insert(self, data):
        if not self.root:
            self.root = Bst(data)
        else:
            self._insert(data, self.root)

    def _search(self, value, current_node):
        if value == current_node.data:
            return True
        elif value < current_node.data and current_node.leftChild:
            return self._search(value, current_node.leftChild)
        elif value > current_node.data and current_node.rightChild:
            return self._search(value, current_node.rightChild)
        return False

    def search(self, value):
        if not self.root:
            return False
        else:
            return self._search(value, self.root)

    def _inorder_traversal(self, current_node):
        traversal = []
        if current_node.leftChild:
            traversal += self._inorder_traversal(current_node.leftChild)
        traversal.append(current_node.data)
        if current_node.rightChild:
            traversal += self._inorder_traversal(current_node.rightChild)
        return traversal

    def inorder_traversal(self):
        if not self.root:
            return []
        else:
            return self._inorder_traversal(self.root)

    

