class TreeNode:
    def __init__(self, key) -> None:
        self.val = key
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self) -> None:
        self.root = None

    def insert(self, val):
        if not self.root:
            self.root = TreeNode(val)
        else:
            current = self.root
            while True:
                if val < current.val:
                    if current.left is None:
                        current.left = TreeNode(val)
                        break
                    else:
                        current = current.left
                elif val > current.val:
                    if current.right is None:
                        current.right = TreeNode(val)
                        break
                    else:
                        current = current.right
                else:
                    break
    
    def search(self, key):
        current = self.root
        while current:
            if current.val == key:
                print('Found')
                return key
            elif current.val < key:
                current = current.right
            elif current.val > key:
                current = current.left
        print('Not found')
        return -1
    
    def insert_rec(self, val):
        self.root = insert_recursive(self.root, val)    
    
    def indorder(self):
        inorder_recursive(self.root)
        print()

def inorder_recursive(root):
    if root:
        inorder_recursive(root.left)
        print(root.val, end=' ')
        inorder_recursive(root.right)

def insert_recursive(root, key):
    if root is None:
        return TreeNode(key)
    else:
        if key <= root.val:
            temp = insert_recursive(root.left, key)
            root.left = temp
            temp.parent = root

        elif key > root.val:
            temp = insert_recursive(root.right, key)
            root.right = temp
            temp.parent = root
        return root    

def minNode(node):
    current = node
    while current.left:
        current = current.left
    return current.val

def maxNode(node):
    current = node
    while current.right:
        current = current.right
    return current.val

def successor(node):
    if node.right:
        return minNode(node.right)
    parent = node.parent
    while parent and parent.right == node:
        node = parent
        parent = parent.parent
    return node

if __name__ == '__main__':
    bst = BinarySearchTree()
    bst.insert_rec(5)
    bst.insert_rec(1)
    bst.insert_rec(8)
    bst.insert_rec(2)
    bst.insert_rec(9)
    bst.insert_rec(4)
    bst.indorder()
    # bst.search(3)

    # print(minNode(bst.root))
    # print(maxNode(bst.root))
    print(successor(bst.root))
