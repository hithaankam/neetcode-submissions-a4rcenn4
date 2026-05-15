class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        arr = []

        for interval in intervals:
            arr.append((interval.start, interval.end))
        arr.sort()
        min_heap = []
        ans = 1

        heapq.heappush(min_heap, arr[0][1])
        for start, end in arr[1:]:
            if min_heap[0] <= start:
                heapq.heappop(min_heap)
            heapq.heappush(min_heap, end)
            ans = max(ans, len(min_heap))
        return ans


