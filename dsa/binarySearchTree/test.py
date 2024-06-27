from bst_balance import height, isBalanced

class TreeNode:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None
        self.height = 1

class AVL:
    def __init__(self) -> None:
        self.root = None

    def height(self, node):
        if not node:
            return 0
        return node.height
    
    def balance_factor(self, node):
        if not node:
            return 0
        bf = self.height(node.left) - self.height(node.right)
        return bf
    
    def insert_value(self, value):
        self.root = self.insert(self.root, value)

    def insert(self, node, value):
        if not node:
            return TreeNode(value)
        if value < node.value:
            node.left = self.insert(node.left, value)
        else:
            node.right = self.insert(node.right, value)
        
        node.height = 1 + max(self.height(node.left), self.height(node.right))

        node = self.rotation(node, value)

        return node

    def rotation(self, node, value):
        balanceFactor = self.balance_factor(node)

        if balanceFactor > 1 and value < node.left.value:
            return self.rotation_rr(node)
        
        elif balanceFactor < -1 and value > node.right.value:
            return self.rotation_ll(node)
        
        elif balanceFactor > 1 and value > node.left.value:
            return self.rotation_lr(node)

        elif balanceFactor < -1 and value < node.right.value:
            return self.rotation_rl(node)
        
        return node
    
    def rotation_ll(self, node):
        child = node.right
        temp = child.left

        child.left = node
        node.right = temp

        node.height = 1 + max(self.height(node.left), self.height(node.right))

        child.height = 1 + max(self.height(child.left), self.height(child.right))

        return child

    def rotation_lr(self, node):
        node.left = self.rotation_ll(node.left)
        return self.rotation_rr(node)

    def rotation_rr(self, node):
        child = node.left
        temp = child.right

        child.right = node
        node.left = temp

        node.height = 1 + max(self.height(node.left), self.height(node.right))

        child.height = 1 + max(self.height(child.left), self.height(child.right))

        return child

    def rotation_rl(self, node):
        node.right = self.rotation_rr(node.right)
        return self.rotation_ll(node)

    def inorder(self, p):
        if p.left:
            self.inorder(p.left)
        print(p.info, end=" ")
        if p.right:
            self.inorder(p.right)

    def inorder_traversal(self):
        if self.root:
            self.inorder(self.root)
    
    def getHeight(self):
        return self.calculateHeight(self.root)
    
    def calculateHeight(self, root):
        if root is None:
            return 0
        lh = self.calculateHeight(root.left)
        rh = self.calculateHeight(root.right)
        return max(lh, rh) + 1

    def preOrder(self, node):
        if node:
            print(node.value, end=' ')
            self.preOrder(node.left)
            self.preOrder(node.right)

myTree = AVL() 
root = None
  
root = myTree.insert(root, 10) 
root = myTree.insert(root, 20) 
root = myTree.insert(root, 30) 
root = myTree.insert(root, 40) 
root = myTree.insert(root, 50) 
root = myTree.insert(root, 25) 
  
"""The constructed AVL Tree would be 
            30 
           /  \ 
         20   40 
        /  \     \ 
       10  25    50"""
  
# Preorder Traversal 
print("Preorder traversal of the", 
      "constructed AVL tree is") 
myTree.preOrder(root) 
print() 
if isBalanced(root):
	print("Tree is balanced")
else:
	print("Tree is not balanced")