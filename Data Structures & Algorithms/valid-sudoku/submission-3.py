class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
       rows = [set() for _ in range(9)]
       cols = [set() for _ in range(9)]
       box = [[set() for _ in range(3)] for _ in range(3)]

       for r in range(9):
        for c in range(9):
            val=board[r][c]
            if val == ".":
                continue
            row_r = r//3
            col_r = c//3

            if (val in rows[r] or val in cols[c] or val in box[row_r][col_r]):
                return False
            rows[r].add(val)
            cols[c].add(val)
            box[row_r][col_r].add(val)
       return True


                
            

            