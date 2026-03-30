class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k = len(s1)
        l = 0

        s1CharFreq: dict[str, int] = {}
        for c in s1:
            if c not in s1CharFreq:
                s1CharFreq[c] = 0
            s1CharFreq[c] += 1

        for r in range(k, len(s2) + 1):
            substr = s2[l:r]
            substrFreq: dict[str, int] = {}
            isPresent = True
            
            for c in substr:
                if c not in substrFreq:
                    substrFreq[c] = 0
                substrFreq[c] += 1

            if isPresent and substrFreq == s1CharFreq:
                return True
            
            l += 1
            r += 1

        return False