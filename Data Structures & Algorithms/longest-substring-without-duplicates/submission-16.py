class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        max_length = 0

        substring = set(s[l:r])
        while r < len(s) and l <= r:
            old_len = len(substring)
            substring.add(s[r])
            if len(substring) == old_len:
                # we have duplicates
                substring.remove(s[l]) # remove left pointer one
                l += 1
            else:
                max_length = max(max_length, len(substring))
                r += 1

        return max_length