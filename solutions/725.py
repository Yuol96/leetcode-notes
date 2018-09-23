"""
{
    "author": "Yucheng Huang",
    "difficulty": "medium",
    "link": "https://leetcode.com/problems/split-linked-list-in-parts/description/",
    "beats": 0.0632,
    "category": ["linked-list"],
    "tags": [],
    "questions": []
}
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    
    def splitListToParts(self, root, k):
        """
        :type root: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        if not root:
            return [None for __ in range(k)]
        else :
            self.L = 0
            p = root
            while p is not None:
                self.L += 1
                p = p.next
        
        step = self.L//k
        delta = self.L - step * k
        
        ret = []
        curr = root
        # print(k,step,delta, self.L)
        for __ in range(k):
            head = None
            if delta > 0:
                delta -= 1
                tmp = 1
            else:
                tmp = 0
            for __ in range(step+tmp):
                if curr:
                    if not head:
                        head = curr
                    tail = curr
                    curr = curr.next
                else :
                    tail = None
            if tail:
                tail.next = None
            ret.append(head)
        return ret
