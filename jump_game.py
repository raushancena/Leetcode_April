class LRUCache:

    def __init__(self, capacity: int):
        self.hash={}
        self.deque=collections.deque()
        self.capacity=capacity
        
    def get(self, key: int) -> int:
        try:
            u=self.hash[key]
            for i in self.deque:
                if(i==key):
                    self.deque.remove(i)
                    break
            self.deque.appendleft(key)
            return u
        except:
            return -1
        
    def put(self, key: int, value: int) -> None:
        try:
            self.hash[key]
            for i in self.deque:
                if(i==key):
                    self.deque.remove(i)
                    break
            self.hash[key]=value
            self.deque.appendleft(key)
        except:
            if(len(self.hash)<self.capacity):
                self.hash[key]=value
                self.deque.appendleft(key)
            else:
                self.hash[key]=value
                top=self.deque[-1]
                self.deque.pop()
                del self.hash[top]
                self.deque.appendleft(key)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)