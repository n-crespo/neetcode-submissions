class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = {}
        m = 0
        j = 0
        MAX = len(set(s))
        for i in range(len(s)):
            x = s[i]
            index = d.get(x, None)
            if index is not None and index >= j:
                j = index + 1
                d[x] = i
            else:
                d[x] = i
                m = max(m, i - j + 1)
                if m == MAX:
                    return m
        return m