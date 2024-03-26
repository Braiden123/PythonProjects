class TreeNode:
    def __init__(self, key): #Create new node
        self.key = key
        self.left = None
        self.right = None

    def __str__(self): #Convert to string
        return str(self.key)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self,key):
        self.root = self._insert(self.root, key)

    def _insert(self, node, key):#Insert the new node into tree
        if node is None:
            return TreeNode(key)
        if key < node.key: #Key less than current node key, insert node as the left child.
            node.left = self._insert(node.left, key)
        elif key > node.key: #Key greater than current node key, insert node as the right child.
            node.right = self._insert(node.right, key)
        return node #Node inserted, return this node to parent to update children.

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key): #DFS
        if node is None or node.key == key:
            return node
        if key < node.key:
            return self._search(node.left, key)
        return self._search(node.right, key)

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        if node is None:
            return node
        if key < node.key: #Node to be deleted is in the left subtree
            node.left = self._delete(node.left, key)
        elif key > node.key: #Node to be deleted is in the right subtree
            node.right = self._delete(node.right, key)
        else:
            if node.left is None: #No left subtree, go to right subtree
                return node.right

            elif node.right is None: #No right subtree, go to left subtree
                return node.left

            node.key = self._min_value(node.right)
            node.right = self._delete(node.right, node.key)
        return node

    def _min_value(self, node):
        while node.left is not None:
            node = node.left
        return node.key

    def inorder_traversal(self):
        result = []
        self._inorder_traversal(self.root, result)
        return result

    def _inorder_traversal(self, node, result):
        if node:
            self._inorder_traversal(node.left, result)
            result.append(node.key)
            self._inorder_traversal(node.right, result)


bst = BinarySearchTree()
nodes = [50, 30, 20, 40, 70, 60, 80]

for node in nodes:
    bst.insert(node)
print("Inorder traversal:", bst.inorder_traversal())
print("Search for 40:", bst.search(40))
bst.delete(40)
print("Inorder traversal after deleting 40:", bst.inorder_traversal())
print("Search for 40:", bst.search(40))