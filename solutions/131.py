"""
{
    "difficulty": "medium",
    "link": "https://leetcode.com/problems/palindrome-partitioning/description/",
    "category": ["DFS"],
    "tags": ["backtracking", "palindrome"],
    "questions": []
}
"""

"""
ATTENTION
	- 如果不是palindrome也不能break，因为可能再多几个字符就是palindrome了！！所以要用continue
"""

def isPalindrome(s):
    i,j = 0,len(s)-1
    while i<j:
        if s[i]!=s[j]:
            return False
        i+=1
        j-=1
    return True

def DFS(s, currPartition, lst):
    if len(s)==0:
        lst.append(currPartition)
        return
    
    for idx in range(1,len(s)+1):
        if not isPalindrome(s[:idx]):
            continue
        DFS(s[idx:], currPartition+[s[:idx]], lst)

class Solution:
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        lst = []
        DFS(s, [], lst)
        return lst