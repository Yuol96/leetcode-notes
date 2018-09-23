"""
{
    "author": "Yucheng Huang",
    "difficulty": "easy",
    "link": "https://leetcode.com/problems/intersection-of-two-linked-lists/description/",
    "beats": 0.4411,
    "category": ["linked-list"],
    "tags": [],
    "questions": []
}
"""

"""
思路
	- （链表A的独立部分长度 + 公共长度） + 链表B的独立部分长度 == （链表B的独立部分长度 + 公共长度） + 链表A的独立部分长度
	- 如果仅仅是要判断两个链表是否存在交点，有以下两种方法：
		- 把第一个链表的结尾接到第二个链表开头，查看有没有环
		- 比较两个链表最后的结点是否相同
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None
        i = headA
        j = headB
        flagA, flagB = 1, 1
        while i is not j:
            if i.next:
                i = i.next
            elif flagA:
                flagA -= 1
                i = headB
            else :
                return None
            if j.next:
                j = j.next
            elif flagB:
                flagB -= 1
                j = headA
            else :
                return None
        return i 
