class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []

        ROWS, COLS = len(heights), len(heights[0])
        # iterate through first row and first column

        pacific = set()
        atlantic = set()

        queue = deque()

        def bfs(starts):
            queue = deque(starts)
            visited = set(starts)
            
            while queue:
                r, c = queue.popleft()

                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nr, nc = r + dr, c + dc

                    if (0 <= nr < ROWS and 0 <= nc < COLS and
                        (nr, nc) not in visited and heights[nr][nc] >= heights[r][c]):
                        visited.add((nr, nc))
                        queue.append((nr, nc))
            return visited

        p_starts, a_starts = [], []
        for c in range(COLS):
            p_starts.append((0, c))
            a_starts.append((ROWS-1, c))
        for r in range(ROWS):
            p_starts.append((r, 0))
            a_starts.append((r, COLS-1))

        pacific = bfs(p_starts)
        atlantic = bfs(a_starts)

        result = []
        for r, c in pacific:
            if (r, c) in atlantic:
                result.append([r, c])
        return result


















        