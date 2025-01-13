class QueueUsingTwoStacks:
    def __init__(self):
        self.stack1 = [] 
        self.stack2 = []  

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


n = int(input())  
queue = QueueUsingTwoStacks()

for _ in range(n):
    query = input().split()
    q_type = int(query[0])

    if q_type == 1: 
        queue.enqueue(int(query[1]))
    elif q_type == 2: 
        queue.dequeue()
    elif q_type == 3:  
        print(queue.front())
