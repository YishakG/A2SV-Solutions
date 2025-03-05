class RecentCounter:

    def __init__(self):
        self.request = []
        self.initial = 0
        

    def ping(self, t: int) -> int:
        self.request.append(t)        
        n = len(self.request)
        
        while self.request and self.request[self.initial] < (t - 3000):
            self.initial += 1
        return n - self.initial
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)