class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []

        ROWS, COLS = len(heights), len(heights[0])
        # iterate through first row and first column

        pacific = set()
        atlantic = set()

        def dfs(r, c, visited, prev_height):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or (r, c) in visited:
                return
            
            current_height = heights[r][c]
            if current_height < prev_height:
                return


            visited.add((r, c))
            dfs(r + 1, c, visited, current_height)
            dfs(r - 1, c, visited, current_height)
            dfs(r, c + 1, visited, current_height)
            dfs(r, c - 1, visited, current_height)
        
        for c in range(COLS):
            dfs(0, c, pacific, heights[0][c])
            dfs(ROWS-1, c, atlantic, heights[ROWS-1][c])
        for r in range(ROWS):
            dfs(r, 0, pacific, heights[r][0])
            dfs(r, COLS-1, atlantic, heights[r][COLS-1])

        result = []
        for r, c in pacific:
            if (r, c) in atlantic:
                result.append([r, c])
        return result


















        