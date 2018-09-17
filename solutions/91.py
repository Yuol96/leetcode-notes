"""
{
    "author": "Yucheng Huang",
    "difficulty": "medium",
    "link": "https://leetcode.com/problems/decode-ways/description/",
    "beats": 0.3665,
    "category": ["BFS","dynamic-programming"],
    "tags": ["integer-break"],
    "questions": []
}
"""

"""
思路：
	- 递推：求前i个字符组成的substring s[:i]的decode方法数量record[i]
"""

"""
ATTENTION
	- 本题最关键的是数字0的处理。
	- 0不能出现在开头，0之前的元素必须是'1'或者'2'
"""

class Solution:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s[0] == '0':
            return 0
        record = [1]
        for idx in range(1,len(s)):
            if s[idx] == '0':
                if s[idx-1] not in ['1','2']:
                    return 0
                if idx>1:
                    record.append(record[idx-2])
                else :
                    record.append(1)
            else :
                tmp = record[idx-1]
                if s[idx-1]!='0' and int(s[idx-1:idx+1])<=26:
                    tmp += record[idx-2]                    
                record.append(tmp)
        # print(record)
        return record[-1]
                
