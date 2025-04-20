# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        dummyNode = ListNode(0)
        curr = dummyNode
        carry = 0 

        while(l1 is not None or l2 is not None or carry):
            sum = carry
            if l1:
                sum = l1.val + sum
                l1 = l1.next
            if l2:
                sum = l2.val + sum
                l2 = l2.next

            newNode = ListNode(sum % 10)
            carry = sum // 10

            curr.next = newNode
            curr = curr.next

        return dummyNode.next
