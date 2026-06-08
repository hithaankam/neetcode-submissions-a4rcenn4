class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_jump = 0
        for i, num in enumerate(nums):
            if i <= max_jump:
                max_jump = max(max_jump, i + num)
            else:
                return False
        return True