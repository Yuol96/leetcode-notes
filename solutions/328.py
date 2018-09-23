"""
{
    "author": "Yucheng Huang",
    "difficulty": "medium",
    "link": "https://leetcode.com/problems/odd-even-linked-list/description/",
    "beats": 1.0000,
    "category": ["linked-list"],
    "tags": [],
    "questions": []
}
"""

"""
思路
	- 把odd和even分别挑出来串成串，再concatenate
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        oddHead = head
        evenHead = head.next
        p = oddHead
        q = evenHead
        while True:
            # print(p.val, q.val)
            if not q.next:
                break
            p.next = q.next
            p = p.next
            if not p.next:
                break
            q.next = p.next
            q = q.next
        p.next = evenHead
        q.next = None
        return oddHead