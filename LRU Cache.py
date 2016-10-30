__author__ = 'wq'

class Node:
    def __init__(self, key, value):
        self.key = key;
        self.value = value;
        self.next = None;
        self.pre = None;

class LRUCache:
    def __init__(self, capacity):
        self.map = {} #(key, Node)
        self.capacity = capacity
        self.head = Node(-1,-1)
        self.tail = Node(-1,-1)
        self.head.next = self.tail
        self.tail.pre = self.head


    def get(self, key):
        if key in self.map:
            self.moveToHead(self.map[key])
            return self.map[key].value
        else:
            return -1

    def set(self,key,value):
        if key in self.map:
            self.map[key].value = value
            self.moveToHead(self.map[key])
        else:
            newNode = Node(key,value)
            self.insertToHead(newNode)
            self.map[key] = newNode

    def moveToHead(self, curNode):
        if curNode is self.head.next:
            return
        else:
            #connect 2 & 4
            curNode.pre.next = curNode.next
            curNode.next.pre = curNode.pre
            #add to head
            curNode.pre = self.head
            curNode.next = self.head.next
            self.head.next.pre = curNode
            self.head.next = curNode
            return

    def insertToHead(self,newNode):
        if self.isFull():
            self.deleteTail()
        newNode.pre = self.head
        newNode.next = self.head.next
        self.head.next.pre = newNode
        self.head.next = newNode

    def isFull(self):
        if len(self.map) >= self.capacity:
            return True
        else:
            return False

    def deleteTail(self):
        deleteNode = self.tail.pre
        deleteNode.pre.next = deleteNode.next
        deleteNode.next.pre = deleteNode.pre
        del self.map[deleteNode.key]
        del deleteNode



myCache = LRUCache(1)
myCache.set(2,1)
print myCache.get(2)
myCache.set(3,2)
print myCache.get(2)
print myCache.get(3)

