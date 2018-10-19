"""
{
    "author": "Yucheng Huang",
    "difficulty": "medium",
    "link": "https://leetcode.com/problems/max-chunks-to-make-sorted/description/",
    "beats": 0.3038,
    "category": ["array"],
    "tags": [],
    "questions": []
}
"""

"""
思路
	- leftArr[i]表示arr[:i+1]中的最大值
	- rightArr[i]表示arr[i+1:]中的最小值
	- 只要arr[:i+1]中的最大值小于arr[i+1:]中的最小值，那么就可以有count+=1
"""

class Solution:
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        L = len(arr)
        leftArr = [arr[0] for __ in range(L)]
        rightArr = [L for __ in range(L)]
        for idx in range(1,L):
            leftArr[idx] = max(leftArr[idx-1],  arr[idx])
        print(leftArr)
        for idx in range(L-2,-1,-1):
            rightArr[idx] = min(rightArr[idx+1], arr[idx+1])
        print(rightArr)
        count = 0
        for idx in range(L):
            if leftArr[idx]>rightArr[idx]:
                continue
            count += 1
        return count