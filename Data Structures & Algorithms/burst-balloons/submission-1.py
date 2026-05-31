from functools import lru_cache
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        balloons = [1] + nums + [1]
        @lru_cache(None)
        def helper(l, r):
            ans = 0
            if l > r:
                return 0
            for k in range(l, r + 1):
                curr = balloons[k] * balloons[l - 1] * balloons[r + 1] + helper(l, k - 1) + helper(k + 1, r)
                ans = max(ans, curr)
                
            return ans 
        n = len(nums)
        return helper(1, n)