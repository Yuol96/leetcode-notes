"""
ATTENTION
	- 避免溢出，可使用mid = l + (r-l)//2
	- 有时候需要考虑item > nums[-1]的情况！！！！！！！
"""


def binarySearch(nums, item, cmp_fn):
	"""
	Input:
		- nums: ordered list
		- item: the number to search of
		- cmp_fn: compare function
	Output:
		- the index of the first element that has the same value as `item`. if not finded, return -1
	"""
	l,r = 0,len(nums)-1
	while True:
		mid = (l+r)//2
		if cmp_fn(nums[mid],item) > 0:
			l = mid
		else :
			r = mid
		if l == r-1:
			break
	if nums[l] == item:
		return l
	elif nums[r] == item:
		return r
	else:
		return -1

def test_binarySearch():
	import numpy as np
	cmp_fn = lambda a,b: a<b
	for __ in range(1000):
		nums = np.random.randint(0,1000,100)
		item = np.random.randint(0,1000)
		nums = sorted(list(nums))
		idx = binarySearch(nums,item,cmp_fn)
		if idx == -1:
			assert item not in set(nums)
		else :
			assert nums.index(item) == idx