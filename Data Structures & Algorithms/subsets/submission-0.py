class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        res = []     # the result with 'leaf node' subsets (aka: final states)
        subset = []  # the current subset (aka: current state)
        
        def dfs(i):

            # out of bound -> go back to the 'leaf nodes'
            if i >= len(nums):

                # add the current final subset/state to the result list
                res.append(subset.copy())
                
                # go one step up in the recursive call
                return

            # the LEFT BRANCH
            subset.append(nums[i]) # add the current state into the subset
            dfs(i + 1)             # go deeper WITH the current element

            # the RIGHT BRANCH
            subset.pop() # delete the previously added element
            dfs(i + 1 )  # go deeper WITHOUT the current element

        dfs(0)     # start the recursive call with the first item from nums
        return res