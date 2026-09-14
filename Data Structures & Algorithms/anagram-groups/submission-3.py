class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # step 1: find anagrams
        # step 2: group anagrams
        # step 3: return desired structure

        h = defaultdict(list) # default value is a list

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            
            h[tuple(count)].append(s)

        return list(h.values())
