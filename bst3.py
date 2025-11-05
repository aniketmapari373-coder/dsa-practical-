#insert search create copy of bst display depth or height of tree
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

    def copy_tree(self, root):
        if root is None: return None
        new_node = Node(root.data)
        new_node.left = self.copy_tree(root.left)
        new_node.right = self.copy_tree(root.right)
        return new_node

    def depth(self, root):
        if root is None: return 0
        return max(self.depth(root.left), self.depth(root.right)) + 1

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.data, end=' ')
            self.inorder(root.right)

bst = BST()
root = copy_root = None

while True:
    print("\n1.Insert 2.Search 3.Copy BST 4.Display Depth 5.Display Inorder 6.Exit")
    ch = int(input("Enter choice: "))
    if ch == 1:
        root = bst.insert(root, int(input("Enter value: ")))
    elif ch == 2:
        print("Found" if bst.search(root, int(input("Enter value to search: "))) else "Not Found")
    elif ch == 3:
        copy_root = bst.copy_tree(root)
        print("BST Copied Successfully! Inorder of Copy:", end=' ')
        bst.inorder(copy_root)
    elif ch == 4:
        print("Depth of Tree:", bst.depth(root))
    elif ch == 5:
        print("Inorder Traversal:", end=' ')
        bst.inorder(root)
    else:
        break
