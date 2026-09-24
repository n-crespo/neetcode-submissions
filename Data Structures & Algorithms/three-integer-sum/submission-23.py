class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        n = len(nums)
        nums.sort()

        for i in range(n):
            # skip if we're on the same target as earlier
            if i > 0 and nums[i] == nums[i-1]:
                continue

            # the list is sorted. if we have positive target, we'll never add to zero
            if nums[i] > 0:
                break

            l = i + 1
            r = n - 1
            target = -nums[i]

            while l < r:
                total = nums[l] + nums[r]
                if total > target:
                    r -= 1
                elif total < target:
                    l += 1
                else:
                    result.append([nums[i], nums[r], nums[l]])
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
                        

        return result