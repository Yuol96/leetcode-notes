"""
{
    "author": "Yucheng Huang",
    "difficulty": "medium",
    "link": "https://leetcode.com/problems/different-ways-to-add-parentheses/description/",
    "category": ["divide-and-conquer"],
    "tags": [],
    "questions": []
}
"""

"""
思路：
    - 返回当前input String的所有可能计算结果（一个list）
    - 需要用try-except来判断是否是一个数，作为递归终止条件
"""

class Solution:

    def divideConquer(self, input):
        try:
            return [int(input)]
        except:
            retlist = []
            for idx,c in enumerate(input):
                if c in ['+','-','*']:
                    alist = self.divideConquer(input[:idx])
                    blist = self.divideConquer(input[idx+1:])
                    for a in alist:
                        for b in blist:
                            if c == '+':
                                retlist.append(a+b)
                            elif c == '-':
                                retlist.append(a-b)
                            else:
                                retlist.append(a*b)
            return retlist

    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        return self.divideConquer(input)


