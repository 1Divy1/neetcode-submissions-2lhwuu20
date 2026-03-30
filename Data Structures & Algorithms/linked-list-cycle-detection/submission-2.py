# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None:
            return False
        
        hashSet = set()

        while head.next != None:
            if head.val not in hashSet:
                hashSet.add(head.val)
                head = head.next
            else:
                return True

        return False