class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        # edge case: only one item
        if len(stones) == 1:
            return stones[0]

        # store stones' items with negative values - O(n)
        maxHeap = [-x for x in stones]

        # create the Max-Heap - O(n)
        heapq.heapify(maxHeap)

        # as long as there is at least one item in the heap - O(n)
        while len(maxHeap) > 1:
            x = heapq.heappop(maxHeap) # - O(log n)
            y = heapq.heappop(maxHeap) # - O(log n)
            print(f"x = {x}, y = {y}")

            # both of them are destroyed -> nothing happens
            if x == y:
                continue
            
            # store the difference
            diff = abs( (-x) - (-y) )
            print(f"diff = {diff}")

            # add the diference into the heap - O(log n)
            heapq.heappush(maxHeap, -diff)
        
        if len(maxHeap) == 1:
            return -maxHeap[0]
        return 0