class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        if nums[0] == target:
            return 0

        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2

            if nums[m] == target:
                return m
            elif nums[m] < target:
                l += 1
                m = (l + r) // 2
            else:
                r -= 1
                m = (l + r) // 2

        return -1