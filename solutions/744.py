"""
{
    "author": "Yucheng Huang",
    "difficulty": "easy",
    "link": "https://leetcode.com/problems/find-smallest-letter-greater-than-target/description/",
    "category": ["binary-search"],
    "tags": [],
    "questions": []
}
"""

"""
ATTENTION
	- 注意这里要找到比item大（而不是>=）的最小元素
	- 需要考虑item>arr[-1]的情况
"""

def binarySearch(arr, item):
    if item >= arr[-1]:
        return len(arr)
    l,r = 0,len(arr)-1
    while True:
        mid = l + (r-l)//2
        if arr[mid] > item:
            r = mid
        elif arr[mid] <= item:
            l = mid
        # print(l,r)
        if l == r-1:
            break
            
    if arr[l] > item:
        return l
    else :
        return r

class Solution:
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        result = binarySearch(letters, target)
        # print("result",result)
        if result == len(letters):
            return letters[0]
        return letters[result]
