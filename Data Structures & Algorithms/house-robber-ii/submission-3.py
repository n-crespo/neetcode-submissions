class Solution:
    def rob(self, nums: List[int]) -> int:
        def hr1(nums):
            rob1, rob2 = 0, 0
    
            # [rob1, rob2, n, n + 1, ...]
            for n in nums:
                temp = max(n + rob1, rob2)
                # either choose current and 
                # one before previous, or only
                # previous..
                rob1 = rob2
                rob2 = temp
            return rob2

        # print(f"{nums[1:]}, {nums[:-1]}")
        return max(hr1(nums[1:]), hr1(nums[:-1]), nums[0])



        