"""
{
    "author": "Yucheng Huang",
    "difficulty": "medium",
    "link": "https://leetcode.com/problems/implement-trie-prefix-tree/description/",
    "beats": 0.0308,
    "category": ["tree"],
    "tags": ["trie"],
    "questions": []
}
"""

"""
思路
	- 定义Node类，每个node需要有一个子节点列表，代表所有可能的值
	- 如上定义的Node类不需要val成员变量
"""

class Node:
    def __init__(self):
        self.childs = [None]*26
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
        for i, c in enumerate(word):
            idx = ord(c) - ord('a')
            if node.childs[idx] is None:
                node.childs[idx] = Node()
            node = node.childs[idx]
            if i == len(word)-1:
                node.isLeaf = True
            
    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        node = self.root
        for c in word:
            idx = ord(c) - ord('a')
            node = node.childs[idx]
            if node is None:
                return False
        return node.isLeaf

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        node = self.root
        for c in prefix:
            idx = ord(c) - ord('a')
            node = node.childs[idx]
            if node is None:
                return False
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)