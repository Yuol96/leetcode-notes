"""
{
    "author": "Yucheng Huang",
    "difficulty": "medium",
    "link": "https://leetcode.com/problems/restore-ip-addresses/description/",
    "category": ["DFS"],
    "tags": ["backtracking"],
    "questions": []
}
"""

"""
ATTENTION
	- 在终止条件的判断上，要考虑s == '' 和 len(currIP)>=4 不同时满足，就需要终止！！
	- 开头为0的字段，数字只能是0！！这是特殊情况
"""

def DFS(s, currIP, st):
    if len(currIP)>=4:
        if s=="":
            st.add('.'.join(map(str, currIP)))
        return
    if s == '':
        return
    
    if s[0] == "0":
        DFS(s[1:], currIP+[0], st)
    else:
        for i in range(1,min(4, len(s)+1)):
            if int(s[:i]) < 256:
                DFS(s[i:], currIP+[int(s[:i])], st)

class Solution:
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if s:
            st = set()
            currIP = []
            DFS(s, currIP, st)
            return list(st)
        return []