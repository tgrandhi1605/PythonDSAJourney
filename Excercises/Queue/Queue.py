from collections import deque

class Queue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, value):
        self.queue.appendleft(value)

    def dequeue(self):
        if self.is_empty:
            return self.queue.pop()
        return None

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)


if __name__ =="__main__":
    q = Queue()
    q.enqueue({
        "name": "Tharun",
        "age": 33
    })
    q.enqueue({
        "name": "Alice",
        "age": 30
    })
    q.enqueue({
        "name": "Bob",
        "age": 25
    })
    print(q.queue)
    q.dequeue()
    print(q.queue)
    print(q.is_empty())
    print(q.size())