class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # USING A MAX-HEAP: time - O(n log n), space - O(n)

        max_heap = []
        hash_map = {}

        for n in nums:
            if n not in hash_map:
                hash_map[n] = 0
            hash_map[n] += 1

        for key, val in hash_map.items():
            max_heap.append([-val, key])

        heapq.heapify(max_heap)

        output = []
        while k > 0:
            _, key = heapq.heappop(max_heap)
            output.append(key)
            k -= 1

        return output