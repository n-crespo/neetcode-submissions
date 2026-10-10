class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # return true if
        # 2 distinct elements that are equal
        # AND distance between them is <= k, meaning abs(i - j) <= k

        L = 0
        window = set()
        for R in range(len(nums)):
            if R - L > k:
                window.remove(nums[L])
                L += 1
            if nums[R] in window:
                return True
            window.add(nums[R])
            
        return False