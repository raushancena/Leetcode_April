class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.l=[]
        self.m=[99999999999]
    def d(self,x):
        if(self.m[-1]>=x):
            self.m.append(x)

    def push(self, x: int) -> None:
        self.l.append(x)
        self.d(x)
        

    def pop(self) -> None:
        if(self.l[-1]==self.m[-1]):
            self.l.pop(-1)
            self.m.pop(-1)
        else:
            self.l.pop(-1)

    def top(self) -> int:
        return self.l[-1]

    def getMin(self) -> int:
        return self.m[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()