"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        # store the nodes in a O(1) retrieve time data structure
        hashset = {None: None}
        curr = head
        while curr:
            # store the value only because nodes on the right haven't been created yet
            node = Node(curr.val)
            hashset[curr] = node
            curr = curr.next
        
        # connect the nodes
        curr = head
        while curr:
            node = hashset[curr]
            node.next = hashset[curr.next]
            node.random = hashset[curr.random]
            curr = curr.next
        
        return hashset[head]