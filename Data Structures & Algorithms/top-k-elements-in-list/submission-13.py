class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # go through nums, put counts in count {}
        # key: num, value: count
        counts = {}

        for num in nums:
            counts[num] = 1 + counts.get(num, 0)

        freqs = [[] for i in range(len(nums) + 1)]

        for num, count in counts.items():
            freqs[count].append(num)

        # iterate through freqs backwards
        result = []
        for i in range(len(freqs) - 1, 0, -1):
            for j in freqs[i]:
                result.append(j)
                if len(result) == k:
                    return result