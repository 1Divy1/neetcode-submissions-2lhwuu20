class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 1:
            return 0

        maxLength = 0
        i, j = 0, 0
        currLongest = ""

        while j < len(s):
            if s[j] not in currLongest:
                currLongest += s[j]
                j += 1
            else:
                maxLength = max(maxLength, len(currLongest))
                i += 1
                currLongest = currLongest[1:]
        
        maxLength = max(maxLength, len(currLongest))
        return maxLength