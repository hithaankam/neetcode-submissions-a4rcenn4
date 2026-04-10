class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for stone in stones:
            heapq.heappush(heap, -stone)
        while len(heap) >= 2:
            x = -heapq.heappop(heap)
            y = -heapq.heappop(heap)
            #print(x, y)
            if abs(x - y) > 0:
            
                heapq.heappush(heap, -abs(x - y))
        if heap:
            return -heap[0]
        return 0