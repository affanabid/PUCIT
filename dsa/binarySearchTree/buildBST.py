class TreeNode:
    def __init__(self, key) -> None:
        self.val = key
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self) -> None:
        self.root = None

    def buildBST(self, inorder, preorder):
        if not inorder or not preorder:
            return None
        
        node_key = preorder.pop(0)
        node = TreeNode(node_key)

        index = inorder.index(node_key)

        node.left = self.buildBST(inorder[:index], preorder)
        node.right = self.buildBST(inorder[index+1:], preorder)

        return node

    def print_in_order(self, root):
        if root:
            self.print_in_order(root.left)
            print(root.val, end=' ')
            self.print_in_order(root.right)

    def print_pre_order(self, root):
        if root:
            print(root.val, end=' ')
            self.print_pre_order(root.left)
            self.print_pre_order(root.right)

# Given traversals
in_order = ['D', 'B', 'E', 'A', 'F', 'C']
pre_order = ['A', 'B', 'D', 'E', 'C', 'F']

# Create the BinaryTree object
bt = BinarySearchTree()

# Construct the tree
root = bt.buildBST(in_order, pre_order.copy())

# Test the construction by printing the traversals of the constructed tree
print("In-order traversal of constructed tree: ")
bt.print_in_order(root)
print("\nPre-order traversal of constructed tree: ")
bt.print_pre_order(root)



         