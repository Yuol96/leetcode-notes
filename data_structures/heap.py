"""
ATTENTION!
	- siftup 函数
		- 要检查 parentIdx>=0
	  	- 递归结束要有 self._heap[idx] = val
  	- siftdown 函数
  		- 注意是 if self.cmp_fn(childVal, val)>0:, 而不是 if self.cmp_fn(val, childVal)>0:
	- pop 函数
		- self.heap 在pop最后一个元素之后有可能成为空的列表，所以需要检查self.size!
"""

# import pdb

class MyHeap: 

	def __init__(self, cmp_fn):
		self._heap = []
		self.cmp_fn = cmp_fn

	@property
	def heap(self):
		return tuple(self._heap)

	@property
	def size(self):
		return len(self._heap)
	
	def _getParentIdx(self, idx):
		return (idx-1)//2

	def _exists(self, idx):
		return idx < self.size

	def _getLeftChildIdx(self, idx):
		return 2*idx + 1

	def _siftup(self, idx, val):
		parentIdx = self._getParentIdx(idx)
		parentVal = self._heap[parentIdx]
		if parentIdx>=0 and self.cmp_fn(val, parentVal)>0:
			self._heap[idx] = parentVal
			self._siftup(parentIdx, val)
		else:
			self._heap[idx] = val

	def _siftdown(self, idx, val):
		leftChildIdx = self._getLeftChildIdx(idx)
		if self._exists(leftChildIdx):
			childIdx = leftChildIdx
			if self._exists(leftChildIdx + 1) and self.cmp_fn(self._heap[leftChildIdx+1], self._heap[leftChildIdx])>0:
					childIdx = leftChildIdx + 1
			childVal = self._heap[childIdx]
			if self.cmp_fn(childVal, val)>0:
				self._heap[idx] = childVal
				self._siftdown(childIdx, val)
			else :
				self._heap[idx] = val
		else:
			self._heap[idx] = val

	def add(self, val):
		self._heap.append(val)
		self._siftup(self.size-1, val)

	def pop(self):
		if self.size:
			top_ele = self._heap[0]
			val = self._heap.pop(-1)
			if self.size:
				self._siftdown(0,val)
			return top_ele



def test_sift_up():
	cmp_fn = lambda a,b: 1 if a>b else 0
	hp = MyHeap(cmp_fn)
	hp._heap = [1,2,3,4,5]
	assert tuple(hp.heap) == (1,2,3,4,5)
	hp._siftup(4, 5)
	assert tuple(hp.heap) == (5,1,3,4,2)

def test_sift_down():
	cmp_fn = lambda a,b: a-b
	hp = MyHeap(cmp_fn)
	# hp._heap = [1,2,3,4,5]
	# hp._siftdown(0,1)
	# assert hp.heap == (3,2,1,4,5)
	hp._heap = [3,4,2,1]
	hp._siftdown(0,3)
	assert hp.heap == (4,3,2,1)

def test_add():
	cmp_fn = lambda a,b: a-b
	hp = MyHeap(cmp_fn)
	for i in [1,2,3,4,5]:
		hp.add(i)
	assert hp.heap == (5,4,2,1,3)

def test_pop():
	cmp_fn = lambda a,b: a-b
	hp = MyHeap(cmp_fn)
	assert hp.pop() is None
	assert hp.heap == tuple()
	for i in [1,2,3,4,5]:
		hp.add(i)
	assert hp.pop() == 5
	assert hp.heap == (4,3,2,1)






