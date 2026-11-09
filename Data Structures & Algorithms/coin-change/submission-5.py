class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        queue = deque([(0, 0)])
        seen = [float("inf")] * (amount + 1)

        while queue:
            current, num_coins = queue.popleft()
            if current <= amount and num_coins < seen[current]:
                # only continue if we've never seen this sum before w/ this few coins
                seen[current] = num_coins
                for coin in coins:
                    if current + coin <= amount:
                        queue.append((current + coin, num_coins + 1))

        return seen[-1] if seen[-1] != float("inf") else -1



