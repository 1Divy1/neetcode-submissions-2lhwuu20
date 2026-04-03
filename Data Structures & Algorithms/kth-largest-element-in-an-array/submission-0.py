class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        min_heap = [-n for n in nums]
        heapq.heapify(min_heap)

        last = 0
        while k > 0:
            last = -heapq.heappop(min_heap)
            k -= 1

        return last