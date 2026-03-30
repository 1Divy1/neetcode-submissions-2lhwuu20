class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0

        l, r, maxL = 0, 1, 1
        currHashSet = set()
        currHashSet.add(s[l])

        while r < len(s):
            if s[r] not in currHashSet:
                currHashSet.add(s[r])
                r += 1
            else:
                currHashSet.discard(s[l])
                l += 1
            maxL = max(maxL, len(currHashSet))

        return maxL