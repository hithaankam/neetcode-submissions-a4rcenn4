class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        times = []
        cars = [(pos, sp) for pos, sp in zip(position, speed) ]
        cars.sort()
        for pos, s in cars:
            dist = target  - pos
            time = dist / s
            times.append(time)
        #print(times)
        fleets = 1
        n = len(times)
        print(cars)
        print(times)
        stack = [times[-1]]
        for i in range(n - 2, -1, -1):
            
            while stack and times[i] > stack[-1]:
                stack.pop()
            if not stack:
                fleets += 1
            stack.append(times[i])

        return fleets
