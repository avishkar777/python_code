class Stack(object):
    def __init__(self, size):
        self.index = []
        self.size = size

    def push(self, data):
        if(self.isFull() != True):
            self.index.append(data)
        else:
            print('Stack overflow')

    def pop(self):
        if(self.isEmpty() != True):
            return self.index.pop()
        else:
            print('Stack is already empty!')

    def isEmpty(self):
        return len(self.index) == []

    def isFull(self):
        return len(self.index) == self.size

    def peek(self):
        if(self.isEmpty() != True):
            return self.index[-1]
        else:
            print('Stack is already empty!')

myStack = Stack(10)
for i in range(0, 10):
    myStack.push(i)
print(myStack.isEmpty())        
print(myStack.isFull())         
print(myStack.index)                        
print(myStack.pop())            
print(myStack.index)                  
print(myStack.peek())
print("***Avishkar_Gautam_33***")


