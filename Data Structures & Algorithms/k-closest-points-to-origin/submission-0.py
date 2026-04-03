import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        # for each point, store [distance, x1, y1]
        minHeap = []
        for x, y in points:
            dist = math.sqrt( (x - 0) ** 2 + (y - 0) ** 2)
            minHeap.append([dist, x, y])

        # create the Min-Heap
        # compare distances; if equal -> compare Xs; if equal -> compare Ys
        # this way, even if two points have the same dist, it will work
        heapq.heapify(minHeap)

        # extract the first k items from the Min-Heap
        # save X and Y from each point to a result list
        output = []
        while k > 0:
            dist, x, y = heapq.heappop(minHeap)
            output.append([x, y])
            k -= 1

        return output