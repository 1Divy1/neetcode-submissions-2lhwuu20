# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next == None:
            return None
        
        dummy = head
        length = 0
        
        while dummy:
            length += 1
            dummy = dummy.next

        prev, dummy = head, head
        for _ in range(length - n):
            prev = dummy
            dummy = dummy.next

        # edge case: node to be deleted is the first one
        if length - n == 0:
            head = dummy.next
            dummy = None
        else:
            prev.next = dummy.next
            dummy.next = None

        return head