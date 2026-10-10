class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # 1, 2, 4, 6
        # 1, 1, 2, 8
        # 48 24 6  1

        n = len(nums)
        l_mult = [1] * n
        r_mult = [1] * n
        for i in range(1, n):
            l_mult[i] = nums[i-1] * l_mult[i-1]
            # print(f"{nums[i-1]} * {l_mult[i-1]}")

        for j in range(n - 2, -1, -1):
            # print(f"adding: {nums[j+1]} * {r_mult[j+1]}")
            r_mult[j] = nums[j+1] * r_mult[j+1]

        # print(f"left: {l_mult}")
        # print(f"right: {r_mult}")
        result = [0] * n
        for i in range(n):
            result[i] = l_mult[i] * r_mult[i]
        return result

        
