class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result = nums[0]

        prefix = nums[0]
        for i in range(1, len(nums)):
            if prefix < 0:
                print(f"setting to: {nums[i]}")
                prefix = 0
            prefix += nums[i]
            result = max(result, prefix)
        return result