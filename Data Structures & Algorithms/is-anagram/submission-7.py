class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sChars = {}
        for c in s:
            sChars[c] = 1 + sChars.get(c, 0)

        tChars = {}
        for c in t:
            tChars[c] = 1 + tChars.get(c, 0)

        if len(sChars) != len(tChars):
            return False
        
        for i in sChars:
            if sChars[i] != tChars.get(i, 0):
                return False

        return True
