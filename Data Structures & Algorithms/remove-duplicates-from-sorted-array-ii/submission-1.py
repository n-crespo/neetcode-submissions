class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 1
        if nums[l] == nums[0]:
            l = 2

        for r in range(1, len(nums)):
            if nums[r] != nums[r - 1] or (r > 1 and  nums[r] != nums[l-2]):
                nums[l] = nums[r]
                l += 1
        return l
        