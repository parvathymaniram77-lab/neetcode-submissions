class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(len(board)):
            seen = []
            for j in range(len(board)):#refer notes for understanding range
                if board[i][j] == ".":
                    continue
                if board[i][j] in seen:
                    return False
                else:
                    seen.append(board[i][j])                

        for j in range(len(board)):
            seen = []
            for i in range(len(board)):
                if board[i][j] == ".":
                    continue
                if board[i][j] in seen:
                    return False
                else:
                    seen.append(board[i][j])
                         
        for i in range(0,9,3):
            for j in range(0,9,3):
                seen = []
                for r in range(i,i+3): #refer notes
                    for c in range(j,j+3):
                        if board[r][c] == ".": 
                            continue
                        if board[r][c] in seen:
                            return False
                        else:
                            seen.append(board[r][c])
        return True



    
