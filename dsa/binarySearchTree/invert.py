# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:

    def __init__(self) -> None:
        self.array = []
    def invertTree(self, root):
        self.traverse(root)
        for num in self.array:
            self.insert(root, num)
        return root
        
    def traverse(self, root):
        if root:
            self.array.append(root.val)
            self.traverse(root.left)
            
            self.traverse(root.right)

    def insert(self, root, val):
        if root is None:
            return TreeNode(val)
        if val == root.val:
            return root
        elif val < root.val:
            root.right = self.insert(root.right, val)
        elif val > root.val:
            root.left = self.insert(root.left, val)
        return root
    
    def inorder(self, root):
        if root:
            self.inorder(root.left)
            # self.array.append(root.val)
            print(root.val, end=' ')

            self.inorder(root.right)
# s = Solution()
# root = TreeNode(2)
# root.left = TreeNode(1)
# root.right = TreeNode(3)

# s.traverse(root)
# print(s.array)
# # s.inorder(root)

a = []
b = []
print(a==b)
