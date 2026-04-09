class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        sorted_nums = list(sorted(list(set(nums))))
        count_map = [0]
        count = 1
        for i in range(1, len(sorted_nums)):
            if abs(sorted_nums[i - 1] - sorted_nums[i]) == 1:
                count += 1
            else:
                count_map.append(count)
                count = 1
        count_map.append(count)
        #count = 1
        return max(count_map)      
