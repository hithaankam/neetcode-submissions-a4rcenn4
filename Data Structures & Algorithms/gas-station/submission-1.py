class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        n = len(gas)
        rem = 0
        start = 0
        for i in range(n):
            rem += gas[i] - cost[i]
            if rem < 0:
                start = (i + 1) % n
                rem = 0
          
            
        return start
