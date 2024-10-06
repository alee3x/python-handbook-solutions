class Stack:

    def __init__(self) -> None:
        self.stack = list()

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        popped = self.stack.pop(len(self.stack) - 1)
        return popped

    def is_empty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False


stack = Stack()
for item in range(10):
    stack.push(item)
while not stack.is_empty():
    print(stack.pop())

stack = Stack()
for item in ("Hello,", "world!"):
    stack.push(item)
while not stack.is_empty():
    print(stack.pop())
