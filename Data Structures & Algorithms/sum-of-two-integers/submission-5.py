class Solution:
    def getSum(self, a: int, b: int) -> int:

        mask = 0xFFFFFFFF
        max_int = 0x7FFFFFFF
        b = b & mask
        a = a & mask

        while (b != 0):
            a, b = a ^ b, (a & b) << 1
            # add without carry, get all carry bits
            # loop back around so that we add back carry

        a = a & mask # drop overflow bits past 31
        return a if a <= max_int else ~(a ^ mask)