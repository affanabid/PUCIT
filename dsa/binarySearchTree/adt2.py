class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    # A utility function to insert a new node with the given key
    def insert(self, node, key):
        # If the tree is empty, return a new node
        if node is None:
            return Node(key)

        # Otherwise, recur down the tree
        if key < node.key:
            node.left = self.insert(node.left, key)
        elif key > node.key:
            node.right = self.insert(node.right, key)

        # return the (unchanged) node pointer
        return node

    def insert_iter(self, key):
        node = Node(key)
        if self.root is None:
            self.root = node
            return
        prev = None
        curr = self.root
        while curr:
            if key < curr.key:
                prev = curr
                curr = curr.left
            else:
                prev = curr
                curr = curr.right
        if key < prev.key:
            prev.left = node
        else:
            prev.right = node

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.key, end=" ")
            self.inorder(root.right)

    def inorder_iter(self):
        curr = self.root
        st = []
        while curr is not None or len(st) != 0:
            if curr:
                st.append(curr)
                curr = curr.left
            else:
                curr = st.pop()
                print(curr.key, end=' ')
                curr = curr.right

    def deleteNode(self, root, key):
        # Base case
        if root is None:
            return root

        # If the key to be deleted is smaller than the root's key, then it lies in the left subtree
        if key < root.key:
            root.left = self.deleteNode(root.left, key)
        # If the key to be deleted is greater than the root's key, then it lies in the right subtree
        elif key > root.key:
            root.right = self.deleteNode(root.right, key)
        # If key is same as root's key, then this is the node to be deleted
        else:
            # Node with only one child or no child
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            # Node with two children: Get the inorder successor (smallest in the right subtree)
            root.key = self.minValue(root.right)

            # Delete the inorder successor
            root.right = self.deleteNode(root.right, root.key)

        return root

    def minValue(self, root):
        minv = root.key
        while root.left:
            minv = root.left.key
            root = root.left
        return minv
 
# Driver Code
if __name__ == "__main__":
    tree = BinaryTree()

    # Let us create following BST
    #        50
    #     /     \
    #    30      70
    #   /  \    /  \
    #  20   40  60   80
    tree.root = tree.insert(tree.root, 50)
    tree.insert_iter(30)
    tree.insert_iter(20)
    tree.insert_iter(40)
    tree.insert_iter(70)
    tree.insert_iter(60)
    tree.insert_iter(80)

    print("Original BST:", end=" ")
    tree.inorder_iter()
    print()

    print("Original BST:", end=" ")
    tree.inorder(tree.root)
    print()

    print("\nDelete a Leaf Node: 20")
    tree.root = tree.deleteNode(tree.root, 20)
    print("Modified BST tree after deleting Leaf Node:")
    tree.inorder_iter()
    print()

    print("\nDelete Node with single child: 70")
    tree.root = tree.deleteNode(tree.root, 70)
    print("Modified BST tree after deleting single child Node:")
    tree.inorder_iter()
    print()

    print("\nDelete Node with both child: 50")
    tree.root = tree.deleteNode(tree.root, 50)
    print("Modified BST tree after deleting both child Node:")
    tree.inorder_iter()
