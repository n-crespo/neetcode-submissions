class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # brute force solution
        if t == "": return ""

        # make frequency hashmap of the required substring
        target = {}
        for char in t:
            target[char] = 1 + target.get(char, 0)

        window_freq = {}
        have, need = 0, len(target)
        result = [-1, -1, float("infinity")]

        l = 0
        for r in range(len(s)):
            char = s[r]

            if char in target:
                # increment window_freq hash
                window_freq[char] = 1 + window_freq.get(char, 0)

                # increment have count only if we've met the condition
                if window_freq[char] == target[char]:
                    have += 1

            while have == need:
                if (r - l + 1) < result[2]:
                    # we have a shorter solution!
                    result[0] = l
                    result[1] = r
                    result[2] = (r - l + 1)
                    # print(f"{result[0]}, {result[1]}")

                # remove from left of the window
                lchar = s[l]

                if lchar in target:
                    window_freq[lchar] -= 1
                    if window_freq[lchar] < target[lchar]:
                        have -= 1
                l += 1

        return s[result[0]:result[1] + 1] if result[2] != float("infinity") else ""
            

        