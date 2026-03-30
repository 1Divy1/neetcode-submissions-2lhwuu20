class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1 and nums[0] == target:
            return 0
        
        secondListStart = 0
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                secondListStart = i
                break

        if secondListStart == 0:
            l, r = 0, len(nums) - 1
            while l <= r:
                m = (l + r) // 2
                if nums[m] == target:
                    return m
                elif nums[m] < target:
                    l += 1
                else:
                    r -= 1
            return -1

        if nums[-1] == target:
            return len(nums) - 1
        elif target < nums[-1]:
            l, r = secondListStart, len(nums) - 1
        else:
            l, r = 0, secondListStart - 1

        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            elif nums[m] < target:
                l += 1
            else:
                r -= 1

        return -1