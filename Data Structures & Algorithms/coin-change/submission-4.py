class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """

        [1, 3, 4] --> 6

        (current_total, num_coins)

        (1, 1) choose 1
            (2, 2) choose 1
            |   (3, 3) choose 1
            |       (4, 4) choose 1
            |           (5, 5) choose 1
            |               (6, 6) choose 1
            (2, 2) choose 3
                (3, 3): choose 1
                (5, 3): choose 3
                (6, 3): choose 4
            (5, 2): total = 5
        (3, 1) choose 3
            (1, 2) choose 1
            (3, 2) choose 3
            (4, 2) choose 4
        (4, 1)
        choose 3: total = 3
        choose 4: total = 4
        """
        result = float("inf")
        queue = deque([(0, 0)])
        seen = [float("inf")] * (amount + 1)

        while queue:
            current, num_coins = queue.popleft()
            if current == amount:
                # we are done
                result = min(result, num_coins)

            if current <= amount and num_coins < seen[current]:
                # only continue if we've never seen this sum before w/ this few coins
                seen[current] = num_coins
                for coin in coins:
                    if current + coin <= amount:
                        queue.append((current + coin, num_coins + 1))

        return result if result != float("inf") else -1


