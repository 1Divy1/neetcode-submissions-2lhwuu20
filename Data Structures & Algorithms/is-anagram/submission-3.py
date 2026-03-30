class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # edge case
        if len(s) != len(t):
            return False

        # character frequencies for s and t
        hashmapS: dict[str, int] = {}
        hashmapT: dict[str, int] = {}
        for i in range(len(s)):
            hashmapS[s[i]] = hashmapS.get(s[i], 0) + 1
            hashmapT[t[i]] = hashmapT.get(t[i], 0) + 1

        # check character match and frequencies
        for char in hashmapS:
            if hashmapS[char] != hashmapT.get(char, 0):
                return False

        return True