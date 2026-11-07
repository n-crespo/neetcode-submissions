class Solution:
    def longestPalindrome(self, s: str) -> str:
        def pal(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            # return last valid bounds
            return l + 1, r - 1

        start, end = 0, 0
        for i in range(len(s)):
            # check odd
            l, r = pal(i, i)
            if r - l > end - start:
                start, end = l, r

            # check even
            l, r = pal(i, i+1)
            if r - l > end - start:
                start, end = l, r
        
        return s[start:end+1]
        