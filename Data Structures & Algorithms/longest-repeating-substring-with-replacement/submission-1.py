class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # uppercase letters s = ""
        # integer k
        # replace any k chars with any uppercase letter

        counts = {}
        res = 0

        l = 0
        max_frequency = 0
        for r in range(len(s)):
            counts[s[r]] = 1 + counts.get(s[r], 0) # incremenet in counts
            max_frequency = max(max_frequency, counts[s[r]])
            
            # NOTE: we don't need to decrement max frequency because
            # if we ever do, we'd be considering a solution that is 
            # worse than what we've seen already.

            if (r - l + 1) - max_frequency <= k:
                res = max(res, r - l + 1)
            else:
                counts[s[l]] -= 1
                l += 1

        return res

        