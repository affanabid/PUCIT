from bst_balance import height, isBalanced

class TreeNode:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def insert(self, root, key):
        if not root:
            return TreeNode(key)
        elif key < root.value:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))

        balanceFactor = self.getBalanceFactor(root)

        # case-1: Left-Left
        if balanceFactor > 1 and key < root.left.value:
            return self.rightRotation(root)
        
        # case-2: Right Right
        elif balanceFactor < -1 and key > root.right.value:
            return self.leftRotation(root)
        
        # case-3: Left Right
        elif balanceFactor > 1 and key > root.left.value:
            root.left = self.leftRotation(root.left)
            return self.rightRotation(root)
        
        elif balanceFactor < -1 and key < root.right.value:
            root.right = self.rightRotation(root.right)
            return self.leftRotation(root)
        
        return root
    
    def delete(self, root,  key):
        if root is None:
            return root
        elif key < root.value:
            root.left = self.delete(root.left, key)
        elif key > root.value:
            root.right = self.delete(root.right, key)
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            
            elif root.right is None:
                temp = root.left
                root = None
                return temp
            
            temp = self.getMinValue(root.right)
            root.value = temp.value
            root.value = self.delete(root.right, temp.value)

        if root is None:
            return root
        
        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))

        balanceFactor = self.getBalanceFactor(root)

        # case-1: Left Left
        if balanceFactor > 1 and self.getBalanceFactor(root.left) >= 0:
            return self.rightRotation(root)
        
        # case-2: Right Right
        elif balanceFactor < -1 and self.getBalanceFactor(root.right) <= 0:
            return self.leftRotation(root)
        
        # case-3: Left-Right
        elif balanceFactor > 1 and self.getBalanceFactor(root.left) < 0:
            root.left = self.leftRotation(root.left)
            return self.rightRotation(root)
        
        # case-4: Right Left
        elif balanceFactor < -1 and self.getBalanceFactor(root.right) > 0:
            root.right = self.rightRotation(root.right)
            return self.leftRotation(root)
        
        return root

    def getMinValue(self, node):
        if root is None or root.left is None:
            return root
        return self.getMinValue(root.left)

    def leftRotation(self, node):
        child = node.right
        temp = child.left
        
        child.left = node
        node.right = temp

        node.height = 1 + max(self.getHeight(node.left), self.getHeight(node.right))

        child.height = 1 + max(self.getHeight(child.left), self.getHeight(child.right))

        return child

    def rightRotation(self, node):
        child = node.left
        temp = child.right

        child.right = node
        node.left = temp

        node.height = 1 + max(self.getHeight(node.left), self.getHeight(node.right))

        child.height = 1 + max(self.getHeight(child.left), self.getHeight(child.right))

        return child
    
    def getHeight(self, root):
        if not root:
            return 0
        return root.height
    
    def getBalanceFactor(self, root):
        if not root:
            return 0
        bf = self.getHeight(root.left) - self.getHeight(root.right)
        return bf
    
    def preOrder(self, root): 
        if not root: 
            return
  
        print("{0} ".format(root.value), end="") 
        self.preOrder(root.left) 
        self.preOrder(root.right) 
    
myTree = AVLTree() 
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