class MyCircularDeque:

    def __init__(self, k: int):
        self.deque=[]
        self.k=k
        

    def insertFront(self, value: int) -> List:
        if len(self.deque)<self.k:
            if self.deque==[]:
                self.deque.append(value)
            else:
                temp=self.deque
                self.deque=[]
                self.deque.append(value)
                self.deque+=temp
            return True
        else:
            return False
    def insertLast(self, value: int) -> bool:
        if len(self.deque)<self.k:
            self.deque.append(value)
            return True
        else:
            return False
        
    def deleteFront(self) -> bool:
        if self.deque:
            self.deque.reverse()
            self.deque.pop()
            self.deque.reverse()
            return True
        else:
            return False

    def deleteLast(self) -> bool:
        if self.deque:
            self.deque.pop()
            return True
        else:
            return False

    def getFront(self) -> int:
        if self.deque:
            return self.deque[0]
        else:
            return -1
        
    def getRear(self) -> int:
        if self.deque:
            return self.deque[-1]
        else:
            return -1
        

    def isEmpty(self) -> bool:
        return self.deque==[]
        

    def isFull(self) -> bool:
        return len(self.deque)==self.k


        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
