class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        h = {}

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            
            key = tuple(count)
            if key not in h:
                h[key] = []
            h[key].append(s)

        return list(h.values())