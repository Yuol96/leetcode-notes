"""
{
    "author": "Yucheng Huang",
    "difficulty": "medium",
    "link": "https://leetcode.com/problems/implement-trie-prefix-tree/description/",
    "beats": 0.2310,
    "category": ["tree"],
    "tags": ["trie"],
    "questions": []
}
"""

"""
思路
	- 定义Node时，用dict代替list，避免稀疏情况占据大量内存
"""

class Node:
    def __init__(self):
        self.childs = {}
        self.isLeaf = False

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()
        

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        node = self.root
        for c in word:
            node.childs[c] = node.childs.get(c, Node())
            node = node.childs[c]
        node.isLeaf = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        node = self.root
        for c in word:
            if c not in node.childs:
                return False
            node = node.childs[c]
        return node.isLeaf

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        node = self.root
        for c in prefix:
            if c not in node.childs:
                return False
            node = node.childs[c]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)