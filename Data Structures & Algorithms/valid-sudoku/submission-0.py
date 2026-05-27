class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows=[set() for _ in range(9)]
        cols=[set() for _ in range(9)]
        boxes=[[set() for _ in range(3)] for _ in range(3)]

        for r in range(9):
            for c in range(9):
                val=board[r][c]

                if val == ".":
                    continue
                
                row_r = r //3
                cols_c = c //3

                if (val in rows[r] or 
                val in cols[c] or 
                val in boxes[row_r][cols_c]):
                   return False

                rows[r].add(val)
                cols[c].add(val)
                boxes[row_r][cols_c].add(val)
        return True


                
            

            