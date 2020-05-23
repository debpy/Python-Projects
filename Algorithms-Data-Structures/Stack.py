class Stack:
    def __init__(self):
        self.items = []

    def push(self, elem):
        self.items = [elem] + self.items

    def pop(self):
        return self.items.pop()
    
stack = Stack()
stack.push(5)
stack.push(7)
stack.push(11)
print(f"Elements after push: {stack.items}")

print(stack.pop())
print(stack.pop())
print(f"Elements after pop: {stack.items}")