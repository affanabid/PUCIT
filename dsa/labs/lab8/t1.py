
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

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert_element_root(self, element):
        if not self.root:
            self.root = Node(element)
            return
        return 'Root element already exists'
    
    def insert_left_child(self, parent, child):
        if parent.left is None:
            parent.left = Node(child)
            return
        return 'Parent already has left child'
    
    def insert_right_child(self, parent, child):
        if parent.right is None:
            parent.right = Node(child)
            return
        return 'Parent already has right child'
    
    def deletion(self, element):
        if self.root == None:
            return None
        if self.root.left == None and self.root.right == None:
            if self.root.key == self.key:
                return None
            else:
                return self.root
        key_node = None
        q = []
        q.append(self.root)
        temp = None
        while(len(q)):
            temp = q.pop(0)
            if temp.value == element:
                key_node = temp
            if temp.left:
                q.append(temp.left)
            if temp.right:
                q.append(temp.right)
        if key_node:
            x = temp.value
            key_node.value = x
            self.deleteDeepest(self.root, temp)
        return self.root
    
    def display_pre_order(self, node):
        self.preorderTraversal(self.root)
        print()

    def display_in_order(self, node):
        self.inorderTraversal(self.root)
        print()

    def display_post_order(self, node):
        self.PostOrderTraversal(self.root)
        print()

    def count_nodes(self): 
        count = self.countHelper(self.root)
        return count
    
    def min_value(self):
        current = self.root
        while current.left is not None:
            current = current.left
        return current.value

    def count_leaf_nodes(self):
        def count_leaves(node):
            if node is None:
                return 0
            if node.left is None and node.right is None:
                return 1
            return count_leaves(node.left) + count_leaves(node.right)

        return count_leaves(self.root)
    
    def non_rec_in_order(self):
        stack = []
        current = self.root
        done = False

        while not done:
            if current is not None:
                stack.append(current)
                current = current.left
            else:
                if len(stack) > 0:
                    current = stack.pop()
                    print(current.value, end=' ') 
                    current = current.right
                else:
                    done = True
        print()

    def non_rec_pre_order(self):
        stack = []
        result = []
        stack.append(self.root)
        while stack:
            current = stack.pop()
            result.append(current.value) 
            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)
        for node in result:
            print(node, end=' ')
        print()

    def non_rec_post_order(self):
        if self.root is None:
            return []
        stack1 = [self.root]
        stack2 = []
        result = []
        while stack1:
            current = stack1.pop()
            stack2.append(current)
            if current.left:
                stack1.append(current.left)
            if current.right:
                stack1.append(current.right)
        while stack2:
            node = stack2.pop()
            result.append(node.value)  # Process the current node (e.g., add its data to the result)
        for node in result:
            print(node, end=' ')
        print()
    
    def find_balance_factor(self, node):
        h1 = self.helperHeight(node.right)
        h2 = self.helperHeight(node.left)
        return h2 - h1

    def display_ancestors(self, node_data):
        self.helperDisplayAncestors(self.root, node_data)
        print()

    def display_descendants(self, node_data):
        descendants = []

        def helper_display_descendants(root, key):
            if root is None:
                return False
            
            if root.data == key:
                return True
        
            if (helper_display_descendants(root.left, key) or
                helper_display_descendants(root.right, key)):
                descendants.append(root.data)
                return True
        
            return False

        helper_display_descendants(self, node_data)
        return descendants
    
    def height_of_tree(self):
        h = self.helperHeight(self.root)
        return h
    
    def helperHeight(self,node):
        if node is None:
            return 0
    
        else:
    
            # Compute the depth of each subtree
            lDepth = self.helperHeight(node.left)
            rDepth = self.helperHeight(node.right)
    
            # Use the larger one
            if (lDepth > rDepth):
                return lDepth+1
            else:
                return rDepth+1
            
    def countHelper(self,node):
        if node is None:
            return 0
        leftCount = self.countHelper(node.left)
        rightCount = self.countHelper(node.right)
        return leftCount + rightCount + 1

    def inorderTraversal(self,node):
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

    def PostOrderTraversal(self, node):
        if node is None:
            return
    
        self.PostOrderTraversal(node.left)
    
        self.PostOrderTraversal(node.right)
        
        print(node.value, end = " ")

    def deleteDeepest(self, root, d_node):
        q = []
        q.append(root)
        while(len(q)):
            temp = q.pop(0)
            if temp is d_node:
                temp = None
                return
            if temp.right:
                if temp.right is d_node:
                    temp.right = None
                    return
                else:
                    q.append(temp.right)
            if temp.left:
                if temp.left is d_node:
                    temp.left = None
                    return
                else:
                    q.append(temp.left)

    def helperDisplayAncestors(self, root, key):
        if root == None:
            return False
        
        if root.data == key:
            return True

        if (self.helperDisplayAncestors(root.left, key) or
            self.helperDisplayAncestors(root.right, key)):
            print(root.data,end=' ')
            return True

        return False

if __name__ == '__main__':
    tree = BinaryTree()
    tree.insert_element_root(5)

    tree.insert_left_child(tree.root,2)
    # tree.insert_left_child(tree.root.left,1)

    tree.insert_right_child(tree.root, 4)

    tree.display_in_order(tree.root)
    tree.non_rec_in_order()

    # tree.deletion(2)

    # tree.display_in_order(tree.root)

    # print(tree.count_nodes())

    # print(tree.find_balance_factor(tree.root))

    # print(tree.height_of_tree())