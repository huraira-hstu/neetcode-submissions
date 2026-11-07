import math

def toBoxNo(row: int, col: int) -> int:
    c = col // 3
    r = row // 3
    return r * 3 + c
     

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [[False for _ in range(9)] for _ in range(9)]
        cols = [[False for _ in range(9)] for _ in range(9)]
        boxes = [[False for _ in range(9)] for _ in range(9)]

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                charVal = ord(board[i][j]) - ord("1")
                
                if (
                    rows[i][charVal]
                    or cols[j][charVal]
                    or boxes[toBoxNo(i, j)][charVal]
                ):
                    return False

                rows[i][charVal] = True
                cols[j][charVal] = True
                boxes[toBoxNo(i,j)][charVal] = True
       
        return True
        


