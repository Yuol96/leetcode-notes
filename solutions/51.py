"""
{
    "difficulty": "hard",
    "link": "https://leetcode.com/problems/n-queens/description/",
    "category": ["DFS"],
    "tags": ["backtracking"],
    "questions": []
}
"""

"""
思路：
    - 对棋盘的每一行做递归，每层递归考虑该行所有可选位置，放置一个Queen，然后标记所有这个Queen可以reach的区域，再进行下一行的递归
"""

class Solution:
    def changeToDot(self, board, i, j, char='.'):
        board[i] = board[i][:j] + char + board[i][j+1:]
    
    def setQueen(self, board, i, j):
        for k in range(self.n):
            self.changeToDot(board, i, k)
            self.changeToDot(board, k, j)
        k = 1
        while i-k >= 0 and j-k >= 0:
            self.changeToDot(board, i-k, j-k)
            k += 1
        k = 1
        while i+k < self.n and j+k < self.n:
            self.changeToDot(board, i+k, j+k)
            k += 1
        k = 1
        while i-k >= 0 and j+k < self.n:
            self.changeToDot(board, i-k, j+k)
            k += 1
        k = 1
        while i+k < self.n and j-k >= 0:
            self.changeToDot(board, i+k, j-k)
            k += 1
        self.changeToDot(board, i, j, 'Q')
        return board

    def DFS(self, board, m):
        if m==0:
            self.ans.append(board)
            return 

        i = self.n - m
        for j,c in enumerate(board[i]):
            if c=='x':
                self.DFS(self.setQueen(board[:], i, j), m-1)
    
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        self.n = n
        self.ans = []
        board = ["x"*self.n for __ in range(self.n)]
        self.DFS(board, n)
        return self.ans

