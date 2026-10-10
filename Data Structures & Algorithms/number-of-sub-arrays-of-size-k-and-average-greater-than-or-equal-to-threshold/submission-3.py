class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        # number of sub-arrays of size k with average >= threshold
        L = 0
        total = 0
        res = 0
        for R in range(len(arr)):
            # get data on newly added num in window
            total += arr[R]

            if R - L + 1 == k:
                avg = total / k
                # print(f"window: {arr[L:R + 1]}, avg: {avg}")
                if avg >= threshold:
                    res += 1
                    
                total -= arr[L]
                L += 1 # shrink window
        return res
