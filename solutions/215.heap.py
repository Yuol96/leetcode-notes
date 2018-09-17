"""
{
	"author": "Yucheng Huang",
    "difficulty": "medium",
	"link": "https://leetcode.com/problems/kth-largest-element-in-an-array/description/",
	"category": ["sort"],
	"tags": ["heap"]
}
"""

"""
K-th element:
	- heap 做法的时间复杂度为O(NlogK), 空间复杂度为O(K)
	- sort 做法的时间复杂度为O(NlogN), 空间复杂度为O(1)
	- quick select 做法的时间复杂度为O(N), 空间复杂度为O(1)
"""

class MyHeap:
    def __init__(self, cmp_fn):
        self.heap = []
        self.cmp_fn = cmp_fn
        
    @property
    def size(self):
        return len(self.heap)
    
    def getParentIdx(self,idx):
        return (idx-1)//2
    
    def getLeftChildIdx(self,idx):
        return 2*idx + 1
    
    def exists(self, idx):
        return idx < self.size
    
    def siftup(self, idx, val):
        parentIdx = self.getParentIdx(idx)
        parentVal = self.heap[parentIdx]
        if parentIdx>=0 and self.cmp_fn(val, parentVal)>0:
            self.heap[idx] = parentVal
            self.siftup(parentIdx, val)
        else:
            self.heap[idx] = val
            
    def siftdown(self, idx, val):
        leftChildIdx = self.getLeftChildIdx(idx)
        if self.exists(leftChildIdx):
            childIdx = leftChildIdx
            if self.exists(leftChildIdx + 1) and self.cmp_fn(self.heap[leftChildIdx + 1], self.heap[leftChildIdx])>0:
                childIdx = leftChildIdx + 1
            childVal = self.heap[childIdx]
            if self.cmp_fn(childVal, val)>0:
                self.heap[idx] = childVal
                self.siftdown(childIdx, val)
            else:
                self.heap[idx] = val
        else:
            self.heap[idx] = val
            
    def add(self, val):
        self.heap.append(val)
        self.siftup(self.size-1, val)
        
    def pop(self):
        if self.size:
            top_ele = self.heap[0]
            val = self.heap.pop(-1)
            if self.size:
                self.siftdown(0, val)
            return top_ele
        

class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        cmp_fn = lambda a,b: a<b
        hp = MyHeap(cmp_fn)
        for num in nums:
            hp.add(num)
            if hp.size > k:
                hp.pop()
        return hp.pop()
