class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevValues = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevValues:
                return [prevValues[diff], i]
            else:
                prevValues[n] = i
            
        