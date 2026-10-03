class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""

        # frequency hash of what we need, hash of our current window
        countT, window = {},  {}

        # we build the frequency hash we want
        for c in t: # target
            countT[c] = 1 + countT.get(c, 0)
            # now we have char: frequency map

        have, need = 0, len(countT) # number of unique items in countT

        # right boundary
        res, resultLen = [-1, -1], float("infinity")
        l = 0
        for r in range(len(s)): 
            current = s[r]

            # update the window hash map to new frequency
            window[current] = 1 + window.get(current, 0)

            # did we satisfy the condition?

            if current in countT and window[current] == countT[current]:
                have += 1
            
            while have == need:
                # update our result
                # size of current window
                if (r - l + 1) < resultLen:
                    res = [l, r]
                    resultLen = (r - l + 1)
                # pop from the left of the window
                window[s[l]] -= 1 # decrement from our hash

                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    # if that was a needed char we removed...
                    have -= 1
                    # shift left pointer by 1

                l += 1

        l, r = res

        return s[l:r+1] if resultLen != float("infinity") else ""













