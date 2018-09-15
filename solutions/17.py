"""
{
    "difficulty": "medium",
    "link": "https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/",
    "category": ["DFS"],
    "tags": ["backtracking"],
    "questions": []
}
"""

"""
思路：
	- 对于每条递归链，需要把上一层的结果，传到下层
"""

digit2chars = {
    2: list('abc'),
    3: list('def'),
    4: list('ghi'),
    5: list('jkl'),
    6: list('mno'),
    7: list('pqrs'),
    8: list('tuv'),
    9: list('wxyz'),
}

def DFS(digits, prefix, st):
    if len(digits)==0:
        st.add(prefix)
        return
    for char in digit2chars[int(digits[0])]:
        DFS(digits[1:], prefix+char, st)

class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits:
            st = set()
            prefix = ""
            DFS(digits, prefix, st)
            return list(st)
        else :
            return []
