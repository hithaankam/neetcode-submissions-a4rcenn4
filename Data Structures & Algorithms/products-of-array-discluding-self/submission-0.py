from functools import reduce
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        for i, num in enumerate(nums):
            if i == 0:
                res.append(reduce(lambda x, y: x * y, nums[i + 1:]))
            else:
                res.append(reduce(lambda x, y: x * y,nums[:i] + nums[i + 1:]))
        return res
        