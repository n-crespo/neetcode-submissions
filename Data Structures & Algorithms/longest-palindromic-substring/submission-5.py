class Solution:
    def longestPalindrome(self, s: str) -> str:

        # if len(s) == 1:
        #     return s[0]
        # if len(s) == 2:
        #     return s[0:2] if s[0] == s[1] else s[0]

        res = s[0]
        resLen = 1
        for i, center in enumerate(s):
            l, r = i, i
            while l-1 >= 0 and r+1 < len(s) and s[l-1] == s[r+1]:
                l -= 1
                r += 1

            # update result if bigger than max
            current = s[l:r+1]
            if current and len(current) > resLen:
                res = current
                resLen = len(current)

            if i + 1 < len(s) and s[i] == s[i+1]:
                l, r = i, i+1
                while l-1 >= 0 and r+1 < len(s) and s[l] == s[r] and s[l-1] == s[r+1]:
                    l -= 1
                    r += 1
    
                # update result if bigger than max
                current = s[l:r+1]
                if current and len(current) > resLen:
                    res = current
                    resLen = len(current)
                

        return res
