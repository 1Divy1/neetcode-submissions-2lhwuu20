class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hashSet = set()
        
        for item in nums:
            if item in hashSet:
                break
            hashSet.add(item)

        return item
        