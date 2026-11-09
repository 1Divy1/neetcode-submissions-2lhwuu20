class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(perm, used):
            if len(perm) == len(nums):
                res.append(perm.copy())
                return
            for n in used:
                if used[n]:
                    continue
                perm.append(n)
                used[n] = True
                backtrack(perm, used)
                perm.pop()
                used[n] = False
        
        backtrack([], {n: False for n in nums})
        
        return res