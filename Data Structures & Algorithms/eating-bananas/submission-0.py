class Solution:
    def can_eat(self, k, h, piles):
        h_k = 0
        for p in piles:
            h_k += math.ceil(p / k)
        return h_k <= h
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)
        ans = -1
        while low <= high:
            mid = (low + high) // 2
            if self.can_eat(mid, h, piles):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans