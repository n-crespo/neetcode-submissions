class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # two pointers
        l, r = 0, 1
        profit = 0

        while r < len(prices):
            if prices[l] > prices[r]:
                # we are buying high, selling low. why not just buy low?
                l = r
            else:
                print(f"profit: {prices[r]} - {prices[l]}")
                profit = max(profit, prices[r] - prices[l])
            r += 1

        return profit
