class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = 9
        for i in range(9):
            s = set()
            t = set()
            for j in range(9):
                if board[i][j] != ".":
                    if board[i][j] in s:
                        return False
                    s.add(board[i][j])
                if board[j][i] != ".":
                    if board[j][i] in t:
                        return False
                    t.add(board[j][i])
        for i in range(3):
            for j in range(3):
                s = set()
                for k in range(3):
                    for l in range(3):
                        val = board[3*i + k][3*j + l]
                        if val != ".":
                            if val in s:
                                return False
                            s.add(val)
        return True
