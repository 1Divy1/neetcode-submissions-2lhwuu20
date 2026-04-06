class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # O(N) - using division operation for the current item
        
        zeros, prod = 0, 1
        for n in nums:
            if n == 0:
                zeros += 1
            else:
                prod *= n

        if zeros > 1:
            return [0] * len(nums)
        
        output = [0] * len(nums)
        for i in range(len(nums)):
            if zeros:
                # 0 if current is zero, else the calculated prod
                output[i] = 0 if nums[i] else prod
            else:
                output[i] = prod // nums[i]

        return output