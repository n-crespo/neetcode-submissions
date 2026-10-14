class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        ROWS, COLS = len(grid), len(grid[0])
        islands = 0 

        # depth first search
        visited = set()
        def dfs(r, c):
            q = deque()
            visited.add((r, c))
            q.append((r, c))

            while q:
                r, c = q.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc
                    if (0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == "1" and (nr, nc) not in visited):
                        q.append((nr, nc))
                        visited.add((nr, nc))

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1' and (r, c) not in visited:
                    dfs(r, c)
                    islands += 1
        return islands

        