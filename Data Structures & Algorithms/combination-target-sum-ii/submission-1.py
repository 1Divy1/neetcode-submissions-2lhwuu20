class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res = []
        candidates.sort()

        def dfs(i, combination, total):
            # base case - adding a new combination
            if total == target:
                res.append(combination.copy())
                return
            
            # base case
            if total > target or i == len(candidates):
                return

            # left branch with the current element
            combination.append(candidates[i])
            dfs(i + 1, combination, total + candidates[i])
            
            # right branch without the current element
            combination.pop()
            # DIFFERENCE FROM Combination Sum I:
            # move to the next element while they're the same
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            dfs(i + 1, combination, total)
        
        dfs(0, [], 0)

        return res