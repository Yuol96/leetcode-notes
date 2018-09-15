"""
{
    "difficulty": "medium",
    "link": "https://leetcode.com/problems/surrounded-regions/description/",
    "category": ["DFS"],
    "tags": [],
    "questions": []
}
"""

class Solution:
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        """
        顺序查找每一个格子，搜索过的格子都标记为“已查找”，如果发现O，就搜索其区域（深度或者广度），判断region内所有点是否有在边界上，若没有，就全部翻转为X，并标记为“已查找”。
        - 考虑board为空的情况
        - 注意搜索区域时，对于每一个点，上下左右都需要搜，而不是只搜右边和下面！！
        """
        if len(board) != 0:
            from queue import Queue
            Lx = len(board)
            Ly = len(board[0])
            # print(Lx,Ly)
            mark = [[0 for __ in range(Ly)] for __ in range(Lx)]
            # print(mark)
            for i in range(Lx):
                for j in range(Ly):
                    if not mark[i][j]:
                        mark[i][j] = 1
                        # print(board[i], i, j)
                        if board[i][j] == "O":
                            q = Queue()
                            lst = []
                            q.put((i,j))
                            while not q.empty():
                                lst.append(q.get())
                                a,b = lst[-1]
                                if a < Lx-1 and not mark[a+1][b]:
                                    mark[a+1][b] = 1
                                    if board[a+1][b] == 'O':
                                        q.put((a+1,b))
                                        
                                if a > 0 and not mark[a-1][b]:
                                    mark[a-1][b] = 1
                                    if board[a-1][b] == 'O':
                                        q.put((a-1,b))
                                    
                                if b < Ly-1 and not mark[a][b+1]:
                                    mark[a][b+1] = 1
                                    if board[a][b+1] == 'O':
                                        q.put((a,b+1))
                                        
                                if b > 0 and not mark[a][b-1]:
                                    mark[a][b-1] = 1
                                    if board[a][b-1] == 'O':
                                        q.put((a,b-1))
                                    
                            flip = True
                            for a,b in lst:
                                if a==Lx-1 or a==0 or b==Ly-1 or b==0:
                                    flip = False
                            if flip:
                                for a,b in lst:
                                    board[a][b] = 'X'
                                
                                
                        
                        