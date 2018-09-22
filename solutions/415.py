"""
{
    "author": "Yucheng Huang",
    "difficulty": "easy",
    "link": "https://leetcode.com/problems/add-strings/description/",
    "beats": 0.8534,
    "category": ["math"],
    "tags": ["string-number"],
    "questions": []
}
"""

class Solution:
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        lst = list("0123456789")
        mapping = {v:idx for idx,v in enumerate(lst)}
        out = [0 for __ in range(max(len(num1), len(num2))+1)]
        i = 0
        num1 = num1[::-1]
        num2 = num2[::-1]
        while i<len(num1) and i<len(num2):
            res = mapping[num1[i]] + mapping[num2[i]] + out[i]
            # print(mapping[num1[i]], mapping[num2[i]], out[i])
            if res>9:
                out[i] = res%10
                out[i+1] = res//10
            else:
                out[i] = res
            # print(res, i, out)
            i+=1
        
        while i<len(num1):
            res = mapping[num1[i]] + out[i]
            if res>9:
                out[i] = res%10
                out[i+1] = res//10
            else:
                out[i] = res
            i+=1
            
        while i<len(num2):
            res = mapping[num2[i]] + out[i]
            if res>9:
                out[i] = res%10
                out[i+1] = res//10
            else:
                out[i] = res
            i+=1
            
        # print(out)
        ret = ''.join(map(str, reversed(out)))
        i = 0
        while i<len(ret)-1 and ret[i] == "0":
            i+=1
        return ret[i:]