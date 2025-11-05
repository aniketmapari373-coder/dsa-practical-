# Q12. Binary Search Tree Operations Operations: a) Insert b) Search c) Display Leaf Nodes d) Level-wise Traversal
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

    def display_leaf(self, root):
        if root:
            if root.left is None and root.right is None:
                print(root.data, end=' ')
            self.display_leaf(root.left)
            self.display_leaf(root.right)

    def level_order(self, root):
        if not root: return
        q = [root]
        while q:
            node = q.pop(0)
            print(node.data, end=' ')
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)

bst = BST()
root = None

while True:
    print("\n1.Insert 2.Search 3.Display Leaf Nodes 4.Level Order 5.Exit")
    ch = int(input("Enter choice: "))
    if ch == 1:
        root = bst.insert(root, int(input("Enter value: ")))
    elif ch == 2:
        print("Found" if bst.search(root, int(input("Enter value to search: "))) else "Not Found")
    elif ch == 3:
        print("Leaf Nodes:", end=' ')
        bst.display_leaf(root)
    elif ch == 4:
        print("Level Order:", end=' ')
        bst.level_order(root)
    else:
        break
