class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 1
        if nums[l] == nums[0]:
            l = 2

        for r in range(1, len(nums)):
            if nums[r] != nums[r - 1] or (r > 1 and  nums[r] != nums[l-2]):
                # if (nums[r] == nums[r-1] and nums[r] != nums[l-2]):
                    # print(f"2 pair: {nums[r-2]}, {nums[r-1]}, {nums[r]}")
                # else:
                    # print(f"mismatch: {nums[r]} != {nums[r-1]}")
                nums[l] = nums[r]
                print(f"adding: {nums[r]}")
                l += 1
        return l
        