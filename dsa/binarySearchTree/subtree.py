class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class BinaryTree:
    def __init__(self):
        self.root = None
        self.array = []

    def insert(self, node, key):
        node = TreeNode(key)
        if self.root is None:
            self.root = node
            return
        prev = None
        curr = self.root
        while curr:
            if key < curr.val:
                prev = curr
                curr = curr.left
            else:
                prev = curr
                curr = curr.right
        if key < prev.val:
            prev.left = node
        else:
            prev.right = node

    def search(self, root, key):
        if root is None:
            return None
        if root.val == key:
            return root
        elif key < root.val:
            return self.search(root.left, key)
        else:
            return self.search(root.right, key)

    def seach(self, root, key):
        if root:
            self.array.append(root.val)

            self.seach(root.left, key)
            self.seach(root.right, key)
def inorder(root):
    if root:
        print(root.val, end=" ")

        inorder(root.left)
        inorder(root.right)

bst = BinaryTree()
# bst.insert(bst.root, 3)
# bst.insert(bst.root, 4)
# bst.insert(bst.root, 5)
# bst.insert(bst.root, 1)
# bst.insert(bst.root, 2)
root = TreeNode(3)
root.left = TreeNode(4)
root.left.left = TreeNode(1)
root.left.right = TreeNode(2)
root.right = TreeNode(5)
bst.seach(root, 5)
print(bst.array)
# inorder(root)
# print(search(root, 6))



