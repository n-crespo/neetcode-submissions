class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        max_length = 0

        substring = set(s[l:r])
        for r in range(len(s)):
            while s[r] in substring:
                # we have a duplicate
                substring.remove(s[l]) 
                l += 1
            substring.add(s[r])
            max_length = max(max_length, r - l + 1)
            r += 1

        return max_length
