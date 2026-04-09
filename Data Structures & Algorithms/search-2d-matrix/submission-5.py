class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n, m = len(matrix), len(matrix[0])
        low, high = 0, n - 1
        floor = -1
        while low <= high:
            mid = (low + high) // 2
            if matrix[mid][0] == target:
                return True
            if matrix[mid][0] > target:
                
                high = mid - 1
            else:
                floor = mid
                low = mid + 1

        low, high = 0, m - 1
        while low <= high:
            mid = (low + high) // 2
            if matrix[floor][mid] == target:
                return True
            if matrix[floor][mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        return False
        