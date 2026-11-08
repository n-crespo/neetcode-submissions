class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        res = set()
        i = 0
        while i < len(nums):
            n = nums[i]
            if n not in res:
                res.add(n)
                i += 1

            else:
                nums.pop(i)

        nums = list(res)
        print(nums)
        return len(res)



        