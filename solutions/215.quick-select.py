"""
{
	"difficulty": "medium",
	"link": "https://leetcode.com/problems/kth-largest-element-in-an-array/description/",
	"category": ["sort"],
	"tags": ["quick-select"]
}
"""

"""
K-th element:
	- heap 做法的时间复杂度为O(NlogK), 空间复杂度为O(K)
	- sort 做法的时间复杂度为O(NlogN), 空间复杂度为O(1)
	- quick select 做法的时间复杂度为O(N), 空间复杂度为O(1)
"""

def partition(nums,l,r,cmp_fn):
	i,j = l,r+1
	pivot = nums[l]
	while True:
		i+=1
		while cmp_fn(nums[i],pivot)>0 and i < r:
			i += 1
		j -= 1
		while cmp_fn(pivot, nums[j])>0 and j > l:
			j -= 1
		if i>=j:
			break
		nums[i], nums[j] = nums[j], nums[i]
	nums[j], nums[l] = nums[l], nums[j]
	return j

def quickSelect(nums, k, cmp_fn):
	l,r = 0, len(nums) - 1
	while l<r:
		j = partition(nums,l,r,cmp_fn)
		if j==k:
			break
		elif j<k:
			l = j+1
		else :
			r = j-1
	return nums[k]
    

class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        cmp_fn = lambda a,b: a>b
        return quickSelect(nums, k-1, cmp_fn)
        








