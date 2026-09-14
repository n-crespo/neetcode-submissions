class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # simple solution: pin a number, check all others for target - pinned

        h = {}
        for i in range(len(nums)):
            j = h.get(target - nums[i], -1)
            if j >= 0:
                return [j, i]
            else:
                h[nums[i]] = i
