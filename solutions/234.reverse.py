"""
{
    "author": "Yucheng Huang",
    "difficulty": "easy",
    "link": "https://leetcode.com/problems/palindrome-linked-list/description/",
    "beats": 0.2239,
    "category": ["linked-list"],
    "tags": [],
    "questions": []
}
"""

"""
思路
	- 把整个链表切成等长两半，把第二段反转。
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseLinkedList(self, head):
        newHead = None
        p = head
        while p is not None:
            newp = p.next
            p.next = newHead
            newHead = p
            p = newp
        return newHead
    
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return True
        if not head.next:
            return True
        p = head
        self.L = 1
        while p is not None:
            self.L += 1
            p = p.next
            
        rIdx = 0
        rNode = head
        while rIdx < self.L//2:
            rIdx += 1
            rNode = rNode.next
            
        rReverseHead = self.reverseLinkedList(rNode)
        
        p,q = head, rReverseHead
        while q is not None:
            if p.val != q.val:
                return False
            p = p.next
            q = q.next
        
        return True
