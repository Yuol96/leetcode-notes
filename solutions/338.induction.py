"""
{
    "author": "Yucheng Huang",
    "difficulty": "medium",
    "link": "https://leetcode.com/problems/counting-bits/description/",
    "beats": 0.9876,
    "category": ["bit manipulation","dynamic-programming"],
    "tags": [],
    "questions": []
}
"""

"""
思路
	- 找规律
	| num  | 二进制数  | 1的个数  |  换一种写法  |
    | ---- | -------- | ------- | ---------- |
    | 0    | 0        | 0       | 0          |
    | 1    | 1        | 1       | 1          |
    | ---- | -------- | ------- | ---------- |
    | 2    | 10       | 1       | 1+0        |
    | 3    | 11       | 2       | 1+1        |
    | ---- | -------- | ------- | ---------- |
    | 4    | 100      | 1       | 1+0        |
    | 5    | 101      | 2       | 1+1        |
    | 6    | 110      | 2       | 1+1        |
    | 7    | 111      | 3       | 1+2        |
    | ---- | -------- | ------- | ---------- |
    | 8    | 1000     | 1       | 1+0        |
    | 9    | 1001     | 2       | 1+1        |
    | 10   | 1010     | 2       | 1+1        |
    | ...  |          |         | ...        |
"""

class Solution:
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        idx = 0
        lst = []
        while idx<=num:
            if idx==0:
                lst.append(0)
                idx += 1
            elif idx==1:
                lst.append(1)
                idx += 1
            else:
                idx += len(lst)
                lst = lst + [1+item for item in lst]
        return lst[:num+1]

##=================================================
## Another version:

class Solution:
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        if num == 0:
            return [0]
        lst = [0 for __ in range(num+1)]
        lst[1] = 1
        base = 1
        idx = 2
        while idx < num+1:
            for i in range(1<<base):
                if idx+i<num+1:
                    lst[idx+i] = 1+lst[i]
            base += 1
            idx = 1<<base
        return lst
