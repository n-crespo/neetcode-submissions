class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = s[0]
        resLen = 1

        for i in range(len(s)):
            l, r = i, i
            while l-1 >= 0 and r+1 < len(s) and s[l-1] == s[r+1]:
                l -= 1
                r += 1

            # update result if bigger than max
            current = s[l:r+1]
            if current and (r - l + 1) > resLen:
                res = current
                resLen = r - l + 1

            if i + 1 < len(s) and s[i] == s[i+1]:
                l, r = i, i+1
                while l-1 >= 0 and r+1 < len(s) and s[l] == s[r] and s[l-1] == s[r+1]:
                    l -= 1
                    r += 1
    
                # update result if bigger than max
                current = s[l:r+1]
                if current and (r - l + 1) > resLen:
                    res = current
                    resLen = r - l + 1
                
        return res