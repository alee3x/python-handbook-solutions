class Queue:

    def __init__(self) -> None:
        self.queue = list()

    def push(self, item):
        self.queue.append(item)

    def pop(self):
        popped = self.queue.pop(0)
        # self.queue.pop(0)
        return popped

    def is_empty(self):
        if len(self.queue) == 0:
            return True
        else:
            return False


queue = Queue()
for item in range(10):
    queue.push(item)
while not queue.is_empty():
    print(queue.pop())

queue = Queue()
for item in ("Hello,", "world!"):
    queue.push(item)
while not queue.is_empty():
    print(queue.pop())
