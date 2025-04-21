# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        curr = head
        count = 0
        while curr:
            curr = curr.next
            count += 1
        
        delen = count - n

        if count == n:
            return head.next
        
        # value = head
        # while value and value.next:
        #     if delen == n-1:
        #         value.next = value.next.next
        #         break
        #     value = value.next
        # return head


        curr = head
        for i in range(delen-1):
            curr = curr.next

        if curr.next:
            curr.next = curr.next.next

        return head
