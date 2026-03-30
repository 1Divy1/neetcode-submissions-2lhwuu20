class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # edge case
        if len(s) != len(t):
            return False

        # character frequencies for s
        hashmap1: dict[str, int] = {}
        for char in s:
            hashmap1[char] = hashmap1.get(char, 0) + 1

        # character frequencies for t
        hashmap2: dict[str, int] = {}
        for char in t:
            hashmap2[char] = hashmap2.get(char, 0) + 1

        # check character match and frequencies
        for char in s:
            if char not in hashmap2 or hashmap1[char] != hashmap2[char]:
                return False

        return True