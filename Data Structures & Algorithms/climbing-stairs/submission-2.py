class Solution:
    def climbStairs(self, n: int) -> int:
        # one, two = 1, 1
        # for i in range(n - 1):
        #     one, two = one + two, one
            # temp = one
            # one = one + two
            # two = temp
        # return one

        n1, n2 = 1, 0
        for _ in range(n):
            n1, n2 = n1 + n2, n1
        return n1
