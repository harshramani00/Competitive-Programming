class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        rows = defaultdict(set)
        cols = defaultdict(set)
        sqr = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in sqr[(r//3,c//3)]:
                    return False
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                sqr[(r//3, c//3)].add(board[r][c])
        return True
# Time Complexity is O(n^2)
