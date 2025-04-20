# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        a = headA
        b = headB
        while (a!=b):
            a = a.next
            b = b.next
            if (a == b):
                return a
            if (a == None):
                a = headB
            if (b == None):
                b = headA
        return a
