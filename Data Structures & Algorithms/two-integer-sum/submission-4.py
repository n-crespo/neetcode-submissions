class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # simple solution: pin a number, check all others for target - pinned

        h = {}
        for i in range(len(nums)):
            if target - nums[i] in h:
                return [h[target-nums[i]], i]
            else:
                h[nums[i]] = i
