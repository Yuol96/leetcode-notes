"""
{
    "author": "Yucheng Huang",
    "difficulty": "hard",
    "link": "https://leetcode.com/problems/sudoku-solver/description/",
    "category": ["DFS"],
    "tags": ["backtracking"],
    "questions": []
}
"""

"""
思路：
    - 找出所有的emptyCells，递归调用DFS，每次递归时取当前的第一个emptycell，找到所有的options，逐个尝试填入，对每种尝试再进行下一次递归
"""

digits = set("123456789")
    
class Solution:
    def getGridRange(self, i):
        if i<3:
            return (0,1,2)
        if i<6:
            return (3,4,5)
        if i<9:
            return (6,7,8)
    
    def getOptions(self, i,j):
        st = set()
        for k in range(self.L):
            if self.board[i][k] in digits:
                st.add(self.board[i][k])
            if self.board[k][j] in digits:
                st.add(self.board[k][j])
        for m in self.getGridRange(i):
            for n in self.getGridRange(j):
                if self.board[m][n] in digits:
                    st.add(self.board[m][n])
        return digits - st
    
    def getEmptyCells(self):
        lst = []
        for i in range(self.L):
            for j in range(self.L):
                if self.board[i][j] == '.':
                    lst.append((i,j))
        return lst
        
    def DFS(self, cells):
        if len(cells) == 0:
            # from copy import deepcopy
            # self.ans = deepcopy(self.board)
            return True
        i,j = cells[0]
        options = self.getOptions(i,j)
        tmp = self.board[i][j]
        for num in options:
            self.board[i][j] = num
            if self.DFS(cells[1:]):
                return True
        self.board[i][j] = tmp
    
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        self.board = board
        self.L = len(board)
        cells = self.getEmptyCells()
        self.DFS(cells)
        


