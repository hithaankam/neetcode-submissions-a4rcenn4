class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def euclid_dist(x, y):
            return math.sqrt(x ** 2 + y ** 2)
        heap = []
        #max_heap
        for pt in points:
            x, y = pt
            dist = euclid_dist(x, y)
            heapq.heappush(heap, (-dist, -x, -y))
            if len(heap) > k:
                heapq.heappop(heap)
        nearest = []
        for d, x, y in heap:
            nearest.append([-x, -y])
        return nearest