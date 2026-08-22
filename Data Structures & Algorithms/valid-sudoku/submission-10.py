class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for i in range(len(board)):
            seen = set()
            for j in range(len(board)):
                if board[i][j] == ".":
                    continue
                if board[i][j] in seen:
                    return False
                
                seen.add(board[i][j])

        for j in range(len(board)):
            seen = set()
            for i in range(len(board)):
                if board[i][j] == ".":
                    continue
                if board[i][j] in seen:
                    return False
                seen.add(board[i][j])

        for i in range(0,9,3):
            for j in range(0,9,3):
                seen = set()
                for r in range(i,i+3):
                    for c in range(j,j+3):
                        if board[r][c] == ".":
                            continue
                        if board[r][c] in seen:
                            return False
                        seen.add(board[r][c])
        return True


                
