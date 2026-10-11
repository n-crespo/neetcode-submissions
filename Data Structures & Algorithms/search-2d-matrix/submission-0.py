class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # this is just binary search but with a flattened matrix
        end = len(matrix) * len(matrix[0])
        row_len = len(matrix[0])
        L, R = 0, end - 1

        while L <= R:
            mid = (L + R) // 2
            val = matrix[mid // row_len][mid % row_len]
            print(f"val: {val}")
            if val > target:
                # we need to shift lower
                R = mid - 1
            elif val < target:
                # we need to shift higher
                L = mid + 1
            else:
                # found it!
                return True

        return False