class MedianFinder:

    def __init__(self):
        self.a = []
        self.b = []
        

    def addNum(self, num: int) -> None:
        if not self.a or num < -self.a[0]:
            heapq.heappush(self.a, -num)
        else:
            heapq.heappush(self.b, num)
        if len(self.a) - len(self.b) > 1:
            heapq.heappush(self.b, -heapq.heappop(self.a))
        if len(self.b) > len(self.a):
            heapq.heappush(self.a, -heapq.heappop(self.b))
        #print(self.a, self.b)
        
        

    def findMedian(self) -> float:
        if len(self.a) > len(self.b):
            return -self.a[0]
        #print(self.a, self.b)
        return (-self.a[0] + self.b[0]) / 2
        