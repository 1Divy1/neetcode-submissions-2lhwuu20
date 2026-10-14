# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        slow = fast = head
        
        while fast and fast.next:
            slow = slow.next  # one step at a time
            fast = fast.next.next  # two steps at a time
            if slow is fast:
                return True
        
        return False