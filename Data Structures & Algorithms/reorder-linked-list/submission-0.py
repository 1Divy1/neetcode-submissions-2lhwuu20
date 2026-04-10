# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        # save each node to a normal list
        nodes = []
        temp = head
        while temp:
            nodes.append(temp)
            temp = temp.next

        # General formula for switches
        # n is even => s = (n // 2) - 1
        # n is odd => s = n // 2
        s = len(nodes) // 2 if len(nodes) % 2 else (len(nodes) // 2) - 1
        print(f"s = {s}")

        # extract the last s nodes from the list and 
        # push them between the current node and the next one
        curr = head
        for _ in range(s):
            lastNode = nodes.pop()

            next = curr.next
            curr.next = lastNode
            lastNode.next = next
            curr = next

        # Edge case: infinite cycle
        # otherwise, the last node will point to another node, not to None
        nodes[-1].next = None