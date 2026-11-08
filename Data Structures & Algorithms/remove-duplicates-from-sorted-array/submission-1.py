class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l, r = 0, 1
        while r < len(nums):
            if nums[l] == nums[r]:
                nums.pop(r)
                print(f"popped! {nums}")
            else:
                print(f"shifting pointers, l at {nums[l]}, r at {nums[r]}")
                l = r
                r += 1

        return l + 1