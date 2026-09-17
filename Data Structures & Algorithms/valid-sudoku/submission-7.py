class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        for row_num, row in enumerate(board):
            for col_num, num in enumerate(row):
                if num == '.': 
                    continue;

                # add to rows hash
                square_num = (row_num // 3, col_num // 3)
                if num in rows[row_num] or num in cols[col_num] or num in squares[square_num]:
                    return False

                rows[row_num].add(num)
                cols[col_num].add(num)
                squares[square_num].add(num)

        return True



                

        # rows[0][1][1] = true