class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l, r = 1, 1
        while r < len(nums):
            if nums[r] != nums[r-1]:
                nums[l] = nums[r]
                l += 1
            r += 1
        return l




        # l, r = 0, 0
        # while r < len(nums):

        #     # skip past all duplicates
        #     while nums[r] == nums[l]:
        #         r += 1

        #     # 0 1 1 1 2
        #     # 

        #     # save the different value
        #     nums[l] = nums[r]
        #     l += 1
        #     r += 1
        # return l + 1