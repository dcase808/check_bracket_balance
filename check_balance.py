from stack import Stack

def is_same(a, b):
    if (a == '{' and b == '}') or (a == '(' and b == ')') or (a == '[' and b == ']'):
        return True
    return False   

def check_brackets_balance(brackets):
    stack = Stack()
    is_balanced = False
    for item in brackets:
        if item in '([{':
            stack.push(item)
        elif is_same(stack.peek(), item):
            stack.pop()
        elif item in ')]}':
            return False
    if stack.is_empty():
        is_balanced = True
    return is_balanced
