class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def set_value(self, value):
        self.value = value

    def set_left(self, left):
        self.left = left

    def set_right(self, right):
        self.right = right

    def get_value(self):
        return self.value
    
    def get_left(self):
        return self.left
    
    def get_right(self):
        return self.right

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def minVal(self, node):
        current = node
        while current.left:
            current = current.left
        return current.value

    def maxVal(self, node):
        current = node
        while node.right:
            node = node.right
        return node.value

    def insert_element(self, value):
        if self.root is None:
            self.root = Node(value)
            return
        else:
            current = self.root
            while True:
                if value < current.value:
                    if current.left is None:
                        current.left = Node(value)
                        break
                    else:
                        current = current.left
                elif value > current.value:
                    if current.right is None:
                        current.right = Node(value)
                        break
                    else:
                        current = current.right
                else:
                    break

    def delete_element(self, value):
        self.root = self.deleteElementRecursive(self.root, value)

    def deleteElementRecursive(self, node, value):
        if node is None:
            return node
        
        if value < node.value:
            node.left = self.deleteElementRecursive(node.left, value)

        elif value > node.value:
            node.right = self.deleteElementRecursive(node.right, value)

        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            
            node.value = self.minVal(node.right)
            
            node.right = self.deleteElementRecursive(node.right, node.value)
        
        return node

    def display_pre_order(self):
        self.preorderTraversal(self.root)
        print()

    def display_in_order(self):
        self.inorderTraversal(self.root)
        print()

    def display_post_order(self):
        self.PostOrderTraversal(self.root)
        print()

    def total_elements(self):
        count = self.helperTotal(self.root)
        print(count)

    def inorderTraversal(self, node):
        if node:
            self.inorderTraversal(node.left)
            print(node.value, end=' ')
            self.inorderTraversal(node.right)

    def preorderTraversal(self,node):
        if node is None:
            return
        print(node.value, end = " ")
    
        self.preorderTraversal(node.left)
    
        self.preorderTraversal(node.right)

    def PostOrderTraversal(self,node):
        if node is None:
            return
    
        self.PostOrderTraversal(node.left)
    
        self.PostOrderTraversal(node.right)
        
        print(node.value, end = " ")

    def helperTotal(self, node):
        if node is None:
            return 0
        
        leftCount = self.helperTotal(node.left)
        rightCount = self.helperTotal(node.right)

        return leftCount + rightCount + 1

if __name__ == '__main__':
    bst = BinarySearchTree()
    # bst.insert_element(5)
    bst.insert_element(7)
    bst.insert_element(2)
    bst.insert_element(8)
    bst.insert_element(0)
    bst.insert_element(3)
    bst.insert_element(5)
    bst.insert_element(4)
    
    bst.display_in_order()

    bst.display_pre_order()

    bst.display_post_order()

    bst.total_elements()
    # bst.delete_element(3)
    # bst.delete_element(10)


    # print(bst.minVal(bst.root))
    # print(bst.maxVal(bst.root))

