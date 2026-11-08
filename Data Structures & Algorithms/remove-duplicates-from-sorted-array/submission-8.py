class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l, r = 1, 1
        while r < len(nums):
            if nums[r] != nums[r-1]:
                # update left pointer with new number!
                nums[l] = nums[r]
                # increment left pointer so we don't overwrite good value
                l += 1
            # keep searching
            r += 1
        return l