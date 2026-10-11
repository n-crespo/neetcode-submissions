class Solution:
    def findMin(self, nums: List[int]) -> int:
        # rotate == shift right
        # all elements are unique
        # minimum element of the array?

        # binary search to find boundary between rotation
        # return left-most part of smaller side

        L = 0
        R = len(nums) - 1

        while L < R:
            mid = (L + R) // 2
            if nums[mid] > nums[R]:
                L = mid + 1
            else:
                R = mid
        return nums[L]