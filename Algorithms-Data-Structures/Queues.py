
#This code is only for illustration, won't work reliably for single item queue
class Queue:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)
        print("Queue elements: {}".format(self.items))

    def pop(self):
        head = self.items[0]
        self.items = self.items[1:]    
        return head

queue = Queue()
queue.push(1)
queue.push(2)
queue.push(3)

print("Popped element: {}".format(queue.pop()))
print("Popped element: {}".format(queue.pop()))
print("Popped element: {}".format(queue.pop()))
print(f"Final items in the queue {queue.items}")