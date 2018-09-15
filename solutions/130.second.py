"""
{
    "difficulty": "medium",
    "link": "https://leetcode.com/problems/surrounded-regions/description/",
    "category": ["DFS"],
    "tags": [],
    "questions": []
}
"""

"""
思路：
	- 先沿着border把所有挨着border的area找到并标记，之后遍历所有点，convert所有未标记的"O"
"""

def DFS(board, i, j, H, W, unchangeSet):
    if board[i][j] == 'O':
        unchangeSet.add((i,j))
        if i>0 and (i-1,j) not in unchangeSet:
            DFS(board, i-1, j, H, W, unchangeSet)
        if i<H-1 and (i+1,j) not in unchangeSet:
            DFS(board, i+1, j, H, W, unchangeSet)
        if j>0 and (i,j-1) not in unchangeSet:
            DFS(board, i, j-1, H, W, unchangeSet)
        if j<W-1 and (i,j+1) not in unchangeSet:
            DFS(board, i, j+1, H, W, unchangeSet)

class Solution:
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if board:
            H = len(board)
            W = len(board[0])
            unchangeSet = set()
            for i in range(W):
                DFS(board, 0, i, H,W, unchangeSet)
                DFS(board, H-1, i, H,W, unchangeSet)
            for i in range(H):
                DFS(board, i, 0, H,W, unchangeSet)
                DFS(board, i, W-1, H,W, unchangeSet)

            for i in range(H):
                for j in range(W):
                    if board[i][j] == 'O' and (i,j) not in unchangeSet:
                        board[i][j] = 'X'