"""
{
    "difficulty": "medium",
    "link": "https://leetcode.com/problems/word-search/description/",
    "category": ["DFS"],
    "tags": ["backtracking"],
    "questions": []
}
"""

"""
ATTENTION
	- 传递board时如果需要标记已访问，可以先改变board[i][j]，递归结束后再改回来
"""

def DFS(board, i, j, word):
    if len(word) == 0:
        return True
    if i<0 or i>=len(board) or j<0 or j>=len(board[0]) or board[i][j] != word[0]:
        return False
    tmp = board[i][j]
    board[i][j] = '*'
    ret = DFS(board, i-1, j, word[1:]) or DFS(board, i+1, j, word[1:]) or DFS(board, i, j-1, word[1:]) or DFS(board, i, j+1, word[1:])
    board[i][j] = tmp
    return ret

class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        for i in range(len(board)):
            for j in range(len(board[0])):
                if DFS(board, i, j, word):
                    return True
        return False