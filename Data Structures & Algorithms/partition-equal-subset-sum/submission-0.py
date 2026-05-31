class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        total = sum(nums)
        def subset_sum(target):
            dp  = [[0] * (target + 1) for _ in range(n + 1)]
            for i in range(n + 1):
                dp[i][0] = 1
            for j in range(1, target + 1):
                dp[0][j] = 1
            for i in range(n + 1):
                for j in range(target + 1):
                    dp[i][j] = dp[i - 1][j]
                    if j - nums[i - 1] >= 0:
                        dp[i][j] += dp[i - 1][j - nums[i - 1]]
            return dp[-1][-1] >= 2
        if total % 2:
            return False
        return subset_sum(total // 2)