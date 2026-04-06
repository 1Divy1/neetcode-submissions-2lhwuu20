class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # O(N^2) - nested for loops (brute force)
        output = [0] * len(nums)
        
        for i in range(len(nums)):
            prod = 1
            for j in range(len(nums)):
                if i == j:
                    continue
                prod *= nums[j]
            output[i] = prod

        return output