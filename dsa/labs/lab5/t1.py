def precedence(operator):
    if operator == '+' or operator == '-':
        return 1
    elif operator == '*' or operator == '/':
        return 2
    elif operator == '^':
        return 3
    else:
        return 0 

def convertToPostfix(infix_expr):
    postfix_expr = ''
    stack = []
    for char in infix_expr:
        # if char.isalnum():  
        if ord(char) >= 48 and ord(char) <= 57:
            postfix_expr += char
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                postfix_expr += stack.pop()
            stack.pop() 
        else:  
            while stack and precedence(stack[-1]) >= precedence(char):
                postfix_expr += stack.pop()
            stack.append(char)
    while stack:
        postfix_expr += stack.pop()
    return postfix_expr

infix_expression = input("Enter an infix expression: ")
postfix_expression = convertToPostfix(infix_expression)
print("Postfix expression:", postfix_expression)
