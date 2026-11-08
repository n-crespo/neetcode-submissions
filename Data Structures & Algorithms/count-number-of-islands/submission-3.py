class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        NUM_ROWS = len(grid)
        NUM_COLS = len(grid[0])
        seen = [[False] * NUM_COLS] * NUM_ROWS
        res = 0

        def bfs(r, c):
            queue = deque([(r, c)])
            while queue:
                r, c = queue.popleft()
                if 0 <= r and r < NUM_ROWS and 0 <= c and c < NUM_COLS and grid[r][c] == "1":
                    # we found land in the valid range
                    grid[r][c] = "0"
                    queue.append((r + 1, c))
                    queue.append((r - 1, c))
                    queue.append((r, c + 1))
                    queue.append((r, c - 1))
            
        for r in range(NUM_ROWS):
            for c in range(NUM_COLS):
                # if we are on land, start searching
                if grid[r][c] != "0":
                    res += 1
                    bfs(r, c)
        return res