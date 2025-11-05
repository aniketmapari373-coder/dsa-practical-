#Q11. Binary Search Tree (BST) Operations: a) Insert b) Delete c) Search d) Traversals (Inorder / Preorder / Postorder)
class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

class BST:
    def insert(self, root, key):
        if root is None: return Node(key)
        if key < root.data: root.left = self.insert(root.left, key)
        elif key > root.data: root.right = self.insert(root.right, key)
        return root

    def search(self, root, key):
        if root is None or root.data == key: return root
        if key < root.data: return self.search(root.left, key)
        return self.search(root.right, key)

    def delete(self, root, key):
        if not root: return root
        if key < root.data: root.left = self.delete(root.left, key)
        elif key > root.data: root.right = self.delete(root.right, key)
        else:
            if not root.left: return root.right
            if not root.right: return root.left
            temp = self.minValueNode(root.right)
            root.data = temp.data
            root.right = self.delete(root.right, temp.data)
        return root

    def minValueNode(self, node):
        while node.left: node = node.left
        return node

    def inorder(self, root):
        if root: self.inorder(root.left); print(root.data, end=' '); self.inorder(root.right)
    def preorder(self, root):
        if root: print(root.data, end=' '); self.preorder(root.left); self.preorder(root.right)
    def postorder(self, root):
        if root: self.postorder(root.left); self.postorder(root.right); print(root.data, end=' ')

bst = BST()
root = None
while True:
    print("\n1.Insert 2.Delete 3.Search 4.Traversal 5.Exit")
    ch = int(input("Enter choice: "))
    if ch == 1:
        root = bst.insert(root, int(input("Enter value: ")))
    elif ch == 2:
        root = bst.delete(root, int(input("Enter value to delete: ")))
    elif ch == 3:
        print("Found" if bst.search(root, int(input("Enter value to search: "))) else "Not Found")
    elif ch == 4:
        print("Inorder:", end=' '); bst.inorder(root)
        print("\nPreorder:", end=' '); bst.preorder(root)
        print("\nPostorder:", end=' '); bst.postorder(root)
    else:
        break
