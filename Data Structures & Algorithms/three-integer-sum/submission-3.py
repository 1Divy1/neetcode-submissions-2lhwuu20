class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        # edge case
        isEdgeCase: bool = True
        for num in nums:
            if num != 0:
                isEdgeCase = False
        if isEdgeCase:
            return [[0, 0, 0]]

        nums.sort()
        output: List[List[int]] = []

        for i, item in enumerate(nums):
            # edge case: no negative numbers in the array
            if item > 0:
                break

            # edge case: if item is a duplicate of the previous item
            if i > 0 and item == nums[i - 1]:
                continue;

            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = item + nums[l] + nums[r]
                
                if threeSum == 0:
                    output.append([item, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                elif threeSum < 0:
                    l += 1
                else:
                    r -= 1

        return output
