"""
{
	"id": 167,
	"name": "Two Sum II - Input array is sorted",
	"difficulty": "easy",
	"link": "https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/",
	"category": ["two pointers"]
}
"""

class Solution:
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        i,j = 0, len(numbers)-1
        flag = False
        while i<j:
            tmp = numbers[i] + numbers[j]
            if tmp < target:
                i += 1
            elif tmp > target:
                j -= 1
            else :
                flag = True
                break
        if flag:
            return [i+1, j+1]
        else:
            print("Error")