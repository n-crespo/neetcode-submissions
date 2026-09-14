class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        sChars = {}
        tChars = {}
        
        for i in range(len(s)):
            sChars[s[i]] = 1 + sChars.get(s[i], 0)
            tChars[t[i]] = 1 + tChars.get(t[i], 0)

        for i in sChars:
            if sChars[i] != tChars.get(i, 0):
                return False

        return True
