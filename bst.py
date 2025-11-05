from collections import deque
# Node structure
class Node:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None
# Binary Search Tree class
class BST:
    def __init__(self):
        self.root = None

    # a) INSERT (with duplicate check)
    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return
        current = self.root
        while True:
            if value == current.val:
                print("Duplicate value ignored!")
                return
            elif value < current.val:
                if current.left is None:
                    current.left = new_node
                    return
                current = current.left
            else:
                if current.right is None:
                    current.right = new_node
                    return
                current = current.right

    # b) SEARCH
    def search(self, value):
        current = self.root
        while current:
            if current.val == value:
                return True
            elif value < current.val:
                current = current.left
            else:
                current = current.right
        return False

    # c) DELETE
    def delete(self, root, key):
        if root is None:
            return None
        if key < root.val:
            root.left = self.delete(root.left, key)
        elif key > root.val:
            root.right = self.delete(root.right, key)
        else:
            # Found node to delete
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            # Two children: find inorder successor
            succ = self.minValueNode(root.right)
            root.val = succ.val
            root.right = self.delete(root.right, succ.val)
        return root

    def minValueNode(self, node):
        while node.left:
            node = node.left
        return node

    # d) TRAVERSALS
    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.val, end=' ')
            self.inorder(node.right)

    def preorder(self, node):
        if node:
            print(node.val, end=' ')
            self.preorder(node.left)
            self.preorder(node.right)

    def postorder(self, node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.val, end=' ')

    # e) DEPTH / HEIGHT
    def height(self, node):
        if node is None:
            return 0
        return 1 + max(self.height(node.left), self.height(node.right))

    # f) MIRROR
    def mirror(self, node):
        if node:
            node.left, node.right = node.right, node.left
            self.mirror(node.left)
            self.mirror(node.right)

    # g) COPY
    def copy(self, node):
        if node is None:
            return None
        new_node = Node(node.val)
        new_node.left = self.copy(node.left)
        new_node.right = self.copy(node.right)
        return new_node

    # h) DISPLAY PARENT → CHILD NODES
    def show_parent_child(self, node):
        if node:
            print(f"Parent: {node.val}", end=' ')
            if node.left:
                print(f"Left: {node.left.val}", end=' ')
            if node.right:
                print(f"Right: {node.right.val}", end=' ')
            print()
            self.show_parent_child(node.left)
            self.show_parent_child(node.right)

    # i) LEAF NODES
    def display_leaves(self, node):
        if node:
            if node.left is None and node.right is None:
                print(node.val, end=' ')
            self.display_leaves(node.left)
            self.display_leaves(node.right)

    # j) LEVEL ORDER
    def level_order(self, node):
        if node is None:
            return
        q = deque([node])
        while q:
            cur = q.popleft()
            print(cur.val, end=' ')
            if cur.left:
                q.append(cur.left)
            if cur.right:
                q.append(cur.right)

# MAIN MENU
def main():
    bst = BST()
    while True:
        print("\n--- Binary Search Tree Operations ---")
        print("1.Insert  2.Search  3.Delete  4.Traversals")
        print("5.Height  6.Mirror  7.Copy  8.Parent-Child")
        print("9.Leaf Nodes  10.Level Order  11.Exit")
        ch = int(input("Enter choice: "))

        if ch == 1:
            val = int(input("Enter value: "))
            bst.insert(val)
        elif ch == 2:
            val = int(input("Enter value to search: "))
            print("Found!" if bst.search(val) else "Not found!")
        elif ch == 3:
            val = int(input("Enter value to delete: "))
            bst.root = bst.delete(bst.root, val)
        elif ch == 4:
            print("Inorder:", end=' ')
            bst.inorder(bst.root); print()
            print("Preorder:", end=' ')
            bst.preorder(bst.root); print()
            print("Postorder:", end=' ')
            bst.postorder(bst.root); print()
        elif ch == 5:
            print("Height:", bst.height(bst.root))
        elif ch == 6:
            bst.mirror(bst.root)
            print("Tree mirrored.")
        elif ch == 7:
            copy_root = bst.copy(bst.root)
            print("Copied tree (inorder):", end=' ')
            bst.inorder(copy_root); print()
        elif ch == 8:
            bst.show_parent_child(bst.root)
        elif ch == 9:
            print("Leaf nodes:", end=' ')
            bst.display_leaves(bst.root); print()
        elif ch == 10:
            print("Level Order:", end=' ')
            bst.level_order(bst.root); print()
        elif ch == 11:
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
