class MinStack:
    
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x: int):
        if not self.stack:
            self.stack.append([x,x])
            return
        curr_min = self.stack[-1][1]
        return self.stack.append([x,min(x,curr_min)])

    def pop(self):
        return self.stack.pop()

    def top(self):
        return self.stack[-1][0]

    def getMin(self):
        return self.stack[-1][1]