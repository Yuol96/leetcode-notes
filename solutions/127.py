"""
{
    "difficulty": "medium",
    "link": "https://leetcode.com/problems/word-ladder/description/",
    "category": ["BFS"],
    "tags": [],
    "questions": []
}
"""

from queue import Queue

class Solution:

    def oneCharDiff(self, a, b):
        if len(a) != len(b):
            return False
        count = 0
        for i in range(len(a)):
            count += (a[i] != b[i])
        return count == 1

    def buildGraph(self, allWords):
        dct = {}
        for i in range(len(allWords)-1):
            for j in range(1,len(allWords)):
                x = allWords[i]
                y = allWords[j]
                if self.oneCharDiff(x,y):
                    dct[x] = dct.get(x,[]) + [x]
                    dct[y] = dct.get(y,[]) + [y]
        return dct

    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        graph = self.buildGraph([beginWord, endWord] + wordList)

        mark = set()
        q = Queue()
        q.put((beginWord,1))
        mark.add(beginWord)
        while not q.empty():
            item, currLen = q.get()
            # print("get item", item, currLen)
            possibleNodes = graph.get(item, [])
            for node in possibleNodes:
                if node not in mark:
                    if node == endWord:
                        return currLen + 1
                    q.put((node, currLen + 1))
                    mark.add(node)
                    # print(currLen, item, node)
        return 0



