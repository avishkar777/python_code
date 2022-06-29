class Queue(object):
    def __init__(self, size):
        self.queue = []
        self.size = size

    def enqueue(self, item):
        if(self.isFull() != True):
            self.queue.insert(0, item)
        else:
            print('Queue is Full!')

    def dequeue(self):
        if(self.isEmpty() != True):
            return self.queue.pop()
        else:
            print('Queue is Empty!')

    def isEmpty(self):
        return self.queue == []

    def isFull(self):
        return len(self.queue) == self.size

            

myQueue = Queue(10)
myQueue.enqueue(4)
myQueue.enqueue(5)
myQueue.enqueue(6)
print(myQueue.queue)
myQueue.dequeue()
print(myQueue.queue)
print("***Avishkar_Gautam_33***")
