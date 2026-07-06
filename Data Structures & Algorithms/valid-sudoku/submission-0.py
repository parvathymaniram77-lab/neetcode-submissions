class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
       
            for i in range(len(board)):
                seen = set()
                for j in range(len(board[i])):
                    if board[i][j] == ".":
                        continue
                    if board[i][j] in seen:
                        return False                      
                    seen.add(board[i][j])                
            

            for j in range(len(board[0])):
                seen = set()
                for i in range(len(board)):
                    if board[i][j] == ".":
                        continue
                    if board[i][j] in seen:
                        return False
                    seen.add(board[i][j])
            

            for startRow in range(0, 9, 3):
                for startCol in range(0, 9, 3):
                    seen = set()

                    for r in range(3):
                        for c in range(3):

                            if board[startRow + r][startCol + c] == ".":
                                continue

                            if board[startRow + r][startCol + c] in seen:
                                return False

                            seen.add(board[startRow + r][startCol + c])

            return True  

            
