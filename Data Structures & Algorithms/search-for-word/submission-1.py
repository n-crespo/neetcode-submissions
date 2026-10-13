class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        path = set()

        # i: current char in target word we are looking for 
        def dfs(r, c, i):
            if i == len(word): 
                return True

            if (not (0 <= r < ROWS and 0 <= c < COLS)
                or word[i] != board[r][c] 
                or (r, c) in path):
                return False
            
            # this tile is in the target word! add to our path
            path.add((r, c))

            # now we try a plus sign around the current tile
            next = i + 1
            res = (dfs(r + 1, c, next) or
                   dfs(r - 1, c, next) or
                   dfs(r, c + 1, next) or
                   dfs(r, c - 1, next))

            path.remove((r, c))
            return res
        
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
        return False