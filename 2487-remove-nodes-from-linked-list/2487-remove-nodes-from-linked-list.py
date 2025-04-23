# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# class Solution(object):
#     def removeNodes(self, head):
#         prev = None
#         curr = head
#         next = None

#         while (curr):
#             next = curr.next
#             curr.next = prev
#             prev = curr
#             curr = next

#         curr1 = prev
#         prev1 = None


#         # while curr1:
#         #     if curr1.next and curr1.next.val < curr.va;:
#         #         prev1.next = curr1
#         #     else:
#         #         # while curr1.next and curr1.next > curr1:
#         #         prev1.next = curr1.next
#         #         prev1 = curr
#         #     curr1 = curr1.next
#         # return prev1.next
                    

            

class Solution(object):
    def removeNodes(self, head):
        # Reverse
        prev = None
        curr = head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        # Remove nodes that have a smaller value than max so far
        max_val = -1  # You chose -1 here
        dummy = ListNode(0)
        dummy.next = prev
        curr = dummy.next
        prev = dummy

        while curr:
            if curr.val >= max_val:
                max_val = curr.val
                prev = curr
            else:
                prev.next = curr.next
            curr = curr.next

        # Reverse again to bring back in its original form
        curr = dummy.next
        prev = None
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        return prev
