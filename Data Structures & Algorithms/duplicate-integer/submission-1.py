class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        # 1. create a hash table (set) from the list
        hashTable: set = set()

        # 2. populate the hash table and check for duplicates
        for item in nums:
            if item in hashTable:
                return True
            else:
                hashTable.add(item)
        
        return False