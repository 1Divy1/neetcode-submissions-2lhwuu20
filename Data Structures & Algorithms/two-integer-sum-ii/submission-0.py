class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left: int = 0
        right: int = len(numbers) - 1

        while left < right:
            if numbers[left] + numbers[right] == target:
                break
            elif numbers[left] + numbers[right] < target:
                left += 1
            else:
                right -= 1
            
        return [left + 1, right + 1]
