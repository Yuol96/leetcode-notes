"""
{
    "author": "Yucheng Huang",
    "difficulty": "easy",
    "link": "https://leetcode.com/problems/palindrome-linked-list/description/",
    "beats": 0.2454,
    "category": ["linked-list"],
    "tags": [],
    "questions": []
}
"""

"""
思路
	- 把整个链表切成等长两半，找到第二段的起始点q，再从第一段递归地找到最后一个点p，比较p和q，相同的话让q往后挪，返回True，继续比较上一层
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def subPalindrome(self, l, lIdx):
        if self.rIdx + lIdx == self.L-1:
            if l.val == self.r.val:
                self.rIdx += 1
                self.r = self.r.next
                return True
            return False
        if self.subPalindrome(l.next, lIdx+1):
            if l.val == self.r.val:
                self.rIdx += 1
                self.r = self.r.next
                return True
            return False
        else :
            return False
    
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
        while p.next is not None:
            p = p.next
            self.L += 1
            
        if self.L%2 == 0:
            rIdx = self.L//2
        else :
            rIdx = self.L//2+1
        i = 0
        p = head
        while p.next is not None:
            i+=1
            p = p.next
            if i == rIdx:
                break
        self.rIdx = rIdx
        self.r = p
        return self.subPalindrome(head, 0)
            
