class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in ans.keys():
                return [ans[complement], i]
            else:
                ans[num] = i