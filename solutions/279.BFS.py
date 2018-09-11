"""
{
    "difficulty": "medium",
    "link": "https://leetcode.com/problems/perfect-squares/description/",
    "category": ["BFS","dynamic-programming"],
    "tags": [],
    "questions": []
}
"""

"""
思路：
    - BFS每一层遍历的节点都与根节点距离相同。设 di 表示第 i 个节点与根节点的距离，推导出一个结论：对于先遍历的节点 i 与后遍历的节点 j，有 di<=dj。利用这个结论，可以求解最短路径等 最优解 问题：第一次遍历到目的节点，其所经过的路径为最短路径。应该注意的是，使用 BFS 只能求解无权图的最短路径。
    - 注意已经访问过的节点要mark，别再访问
"""

from queue import Queue

class Solution:

    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        mark = set()
        q = Queue()
        q.put((n,0))
        mark.add(n)
        while not q.empty():
            item, currLen = q.get()
            # print("get item",item)
            for i in range(1,int(item**0.5)+1):
                node = item - i**2
                if node == 0:
                    return currLen + 1
                if node > 0 and node not in mark:
                    q.put((node, currLen + 1))
                    mark.add(node)
                    # print(currLen, item, node, mark)
