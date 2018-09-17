"""
{
    "author": "Yucheng Huang",
    "difficulty": "medium",
    "link": "https://leetcode.com/problems/friend-circles/description/",
    "category": ["DFS"],
    "tags": [],
    "questions": []
}
"""

def DFS(M, i, j):
    if M[i][j] == 1:
        M[i][j] = 0
        M[j][i] = 0
        for k in range(len(M[i])):
            if M[i][k] == 1:
                DFS(M, i, k)
        if i != j:
            for k in range(len(M[j])):
                if M[j][k] == 1:
                    DFS(M, j, k)

# def printM(M):
#     for lst in M:
#         output = ""
#         for item in lst:
#             output += "{} ".format(item)
#         print(output)
#     print('-'*15)
                
class Solution:
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        count = 0
        if M:
            L = len(M)
            for i in range(L):
                for j in range(i, L):
                    if M[i][j]:
                        count += 1
                        DFS(M, i, j)
                        # print(i,j)
                        # printM(M)
            return count
        else:
            return 0
        