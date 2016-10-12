__author__ = 'wq'
class Queue:
    def __init__(self, capacity):
        self.cap = capacity
        self.array = [0 for i in range(self.cap)]
        self.front = 0
        self.end = 0
        self.size = 0
    def nextIndex(self, i ):
        if i == self.cap - 1:
            return 0
        else:
            return i + 1

    def dequeue(self, x):
        if self.isEmpty():
            return False
        front = self.array[self.front]
        self.front = self.nextIndex(self.front)
        return True

    def enqueue(self, x):
        if self.isFull():
            return False
        self.array[self.end] = x
        self.end = self.nextIndex(self.end)
        return True

    def isFull(self):
        return self.size == self.cap

    def isEmpty(self):
        return self.size == 0

    def getFront(self):
        return self.array[self.front]