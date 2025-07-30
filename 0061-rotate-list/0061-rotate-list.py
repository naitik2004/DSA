class Solution(object):
    def rotateRight(self, head, k):
        if not head:
            return None

        lastele = head
        length = 1

        while (lastele.next):
            lastele = lastele.next
            length += 1
        
        k = k % length

        lastele.next = head

        temp = head

        for _ in range(length - k - 1):
            temp = temp.next

        ans = temp.next
        temp.next = None
        return ans