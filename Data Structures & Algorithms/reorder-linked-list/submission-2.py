class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        # find the middle
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        l2 = slow.next
        slow.next = None  

        # reverse the second sublist
        curr = l2
        prev = None
        while curr:
            nxt = curr.next   
            curr.next = prev
            prev = curr
            curr = nxt
        l2 = prev              

        # merge one by one
        l1 = head             
        while l2:
            n1, n2 = l1.next, l2.next
            l1.next = l2
            l2.next = n1
            l1, l2 = n1, n2