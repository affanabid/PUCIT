class StackNode:
    def __init__(self, val):
        self.info = val
        self.next = None

class Stack:
    def __init__(self) -> None:
        self.top = None

    def is_empty(self):
        if self.top == None:
            return True
        return False
    
    def push(self, val):
        newNode = StackNode(val)
        newNode.next = self.top
        self.top = newNode

    def pop(self):
        current = self.top
        if current is None:
            print('Empty stack')
            return 
        # print(current.info)
        self.top = current.next

        return current.info
        del current

    def peek(self):
        if self.top is None:
            print('Stack empty')
            return
        print(self.top.info)

    def size(self):
        current = self.top
        count = 0
        while current is not None:
            count += 1
            current = current.next
        return count
    
    def display(self):
        current = self.top
        while current is not None:
            print(current.info, end=' ')
            current = current.next
        print()

    def parantheses(self, string):
        for i in range(len(string)):
            if string[i]=='{' or string[i]=='[' or string[i]=='(' :
                self.push(string[i])
    
            elif string[i]=='}' or string[i]==']' or string[i]==')' :
                self.pop()
    
        if not self.is_empty():
            return  False
        else:
            return True

def paranthesescheck(string):
    opening_parantheses = '[{('
    closing_parantheses = ')]}'
    
    pair = {')': '(', ']': '[', '}': '{'}
    dt = Stack()

    for i in range(len(string)):
        if string[i] in opening_parantheses:
            dt.push(string[i])

        elif string[i] in closing_parantheses:
            if not dt.is_empty() and dt.peek() == pair[string[i]]:
                dt.pop()
            else:
                return False

    if not dt.is_empty():
        return False
    else:
        return True

def reverse_string(string):
    word=string.split()
    for i in range(len(word)):
        s=Stack()
        for j in range(len(word[i])):
            s.push(word[i][j])
        for k in range(s.size()):
            print(s.pop(),end='')
        print(end=" ")
stack = Stack()
# print(stack.parantheses('(faiq))'))
# print(paranthesescheck('(faiq))'))
# reverse_string('Welcome to DSA')
stack.push(5)
stack.push(4)
stack.push(3)
stack.push(4)

stack.display()
# stack.pop()
# stack.display()
# stack.peek()
# print(stack.size())

# print(stack.is_empty())