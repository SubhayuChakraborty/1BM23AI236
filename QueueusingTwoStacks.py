class QueueUsingTwoStacks:
    def __init__(self):
        self.stack1 = []  # Stack for enqueue
        self.stack2 = []  # Stack for dequeue

    def enqueue(self, value):
        self.stack1.append(value)

    def dequeue(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        self.stack2.pop()

    def front(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2[-1]

# Input reading
n = int(input())  # Number of queries
queue = QueueUsingTwoStacks()

for _ in range(n):
    query = input().split()
    q_type = int(query[0])

    if q_type == 1:  # Enqueue
        queue.enqueue(int(query[1]))
    elif q_type == 2:  # Dequeue
        queue.dequeue()
    elif q_type == 3:  # Print front
        print(queue.front())
