class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        return self.items.append(item)
    
    def pop(self):
        return self.items.pop()
    
    def is_empty(self):
        return True if self.items == [] or self.items == None else False

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
