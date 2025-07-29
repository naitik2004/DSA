class MyQueue(object):

    def __init__(self):
        self.s1 = []
        self.s2 = []
        
    def push(self, x):
        while self.s1:
            self.s2.append(self.s1.pop())
        self.s1.append(x)
        while self.s2:
            self.s1.append(self.s2.pop())

    def pop(self):
        if not self.s1:
            return None
        return self.s1.pop()

    def peek(self):
        if not self.s1:
            return None
        return self.s1[-1]

    def empty(self):
        return len(self.s1) == 0