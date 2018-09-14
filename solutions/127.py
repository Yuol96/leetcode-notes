"""
{
    "difficulty": "medium",
    "link": "https://leetcode.com/problems/word-ladder/description/",
    "category": ["BFS"],
    "tags": [],
    "questions": []
}
"""

"""
ATTENTION：
    - 如果wordList太长，那么无论是build一个graph还是在wordList中一个一个word查找，都会超时！！！
    - 相反，由于题目说明只会有一个字母有差别，而字母总共只有26个，所以每个单词总共相差1个字母的单词最多是25*len(word)个！！！
"""

from queue import Queue

class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        wordSet = set(wordList)
        mark = set()
        q = Queue()
        q.put((beginWord,1))
        mark.add(beginWord)
        while not q.empty():
            word, currLen = q.get()
            # print("get item", item, currLen)
            for idx,c in enumerate(word):
                for new_c in list('abcdefghijklmnopqrstuvwxyz'):
                    if new_c == c:
                        continue
                    else :
                        new_word = word[:idx] + new_c + word[idx+1:]
                        if new_word in wordSet and new_word not in mark:
                            if new_word == endWord:
                                return currLen + 1
                            mark.add(new_word)
                            q.put((new_word, currLen+1))
        return 0


#------------------------------------- code below will be "time limit exceeded"
# from queue import Queue

# class Solution:

#     def oneCharDiff(self, a, b):
#         if len(a) != len(b):
#             return False
#         count = 0
#         for i in range(len(a)):
#             count += (a[i] != b[i])
#         return count == 1

#     def word2int(self, word):
#         num = 0
#         for c in word:
#             num += ord(c)
#         return num

#     def buildGraph(self, allWords):
#         dct = {}
#         for i in range(len(allWords)-1):
#             for j in range(1,len(allWords)):
#                 x = allWords[i]
#                 y = allWords[j]
#                 if self.oneCharDiff(x,y):
#                     dct[x] = dct.get(x,[]) + [x]
#                     dct[y] = dct.get(y,[]) + [y]
#         return dct
        
#     def ladderLength(self, beginWord, endWord, wordList):
#         """
#         :type beginWord: str
#         :type endWord: str
#         :type wordList: List[str]
#         :rtype: int
#         """
#         graph = self.buildGraph([beginWord, endWord] + wordList)

#         mark = set()
#         q = Queue()
#         q.put((beginWord,1))
#         mark.add(beginWord)
#         while not q.empty():
#             item, currLen = q.get()
#             # print("get item", item, currLen)
#             possibleNodes = graph.get(item, [])
#             for node in possibleNodes:
#                 if node not in mark:
#                     if node == endWord:
#                         return currLen + 1
#                     q.put((node, currLen + 1))
#                     mark.add(node)
#                     # print(currLen, item, node)
#         return 0
#-------------------------------------


