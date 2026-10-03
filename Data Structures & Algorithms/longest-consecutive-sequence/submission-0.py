class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash_set = set(nums)
        longest_seq = 0

        for n in hash_set:
            # not a starting sequence
            if n-1 in hash_set:
                continue
            temp = n
            longest_seq_local = 1
            while temp + 1 in hash_set:
                longest_seq_local += 1
                temp += 1
            if longest_seq_local > longest_seq:
                longest_seq = longest_seq_local

        return longest_seq