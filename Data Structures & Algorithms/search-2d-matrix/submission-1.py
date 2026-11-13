class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        def pos(i: int) -> [int, int]:
            row = i // n
            col = i % n
            return [row, col]

        l, r = 0, (m * n) - 1

        while l <= r:
            mid = l + (r - l) // 2
            row, col = pos(mid)
            midVal = matrix[row][col]

            if midVal == target:
                return True
            elif midVal > target:
                r = mid - 1
            else:
                l = mid + 1
        return False

