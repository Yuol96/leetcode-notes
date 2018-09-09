"""
quick select algorithm
	- note that k is zero-based
	- partition function is the key component
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