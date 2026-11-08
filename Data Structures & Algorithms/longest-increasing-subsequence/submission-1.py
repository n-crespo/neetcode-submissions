class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        lis = [1] * len(nums)
        maxLen = 0

        for i in range(len(nums)-1, -1, -1):
            # print(f"checking i:{i}")
            current = nums[i]
            # go to every index after current
            for j in range(i + 1, len(nums)):
                if current < nums[j]:
                    lis[i] = max(lis[i], 1 + lis[j])
            maxLen = max(maxLen, lis[i])

        return maxLen