class MinStack:

    def __init__(self):
        self.stack=[]
        self.minVal=None
        

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(val)
            self.minVal=val
        else:
            if val>self.minVal:
                self.stack.append(val)
            else:
                temp=2*val-self.minVal
                self.stack.append(temp)
                self.minVal=val
        return None
        

    def pop(self) -> None:
        if self.stack:
            if self.stack[-1]>self.minVal:
                self.stack.pop()
            else:
                self.minVal=2*self.minVal - self.stack[-1]
                self.stack.pop()
                
        

    def top(self) -> int:
        if self.stack[-1]>self.minVal:
            return self.stack[-1]
        else:
            return self.minVal
        

    def getMin(self) -> int:
        return self.minVal
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
