class Stack:
    def __init__(self, n = 5):
        self.items = []
        self.top = -1
        self.size = n

    def push(self, val):
        if(self.isFull()):
            print('Stack Overflow!')          
        else:
            self.items.append(val)
            self.top += 1

    def pop(self):
        if(self.top == -1):
            print('Stack Underflow!')
        else:
            self.top -= 1
            return(self.items.pop())

    def display(self):
        for item in reversed(self.items):
            print(item)

    def isFull(self):
        if(self.top == self.size - 1):
            return True
        else:
            return False

    def peek(self):
        if(self.top == -1):
            print('Cannot peek into an Empty Stack!')
        else:
            print(self.items[self.top])
            