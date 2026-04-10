class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        heap = []
        cooldown = {}
        for task, count in freq.items():
            heapq.heappush(heap, (-count, task))
            cooldown[task] = -1
        time = 0
        while heap:
            cnt, task = heapq.heappop(heap)
            cnt = -cnt
            temp = []
            while cooldown[task] >= time:
                temp.append((cnt, task))
                if not heap:
                    break
                cnt, task = heapq.heappop(heap)
                cnt = -cnt
            if cooldown[task] < time:
                cnt -= 1
                if cnt > 0:
                    heapq.heappush(heap, (-cnt, task))
                    cooldown[task] = time + n
            for cnt, task in temp:
                heapq.heappush(heap, (-cnt, task))
            #print(heap, cooldown)
            time += 1
        return time

