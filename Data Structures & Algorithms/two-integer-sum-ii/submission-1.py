class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        idx1, idx2 = 0, len(numbers) - 1
        result = []

        while idx1 < idx2:
            if numbers[idx1] + numbers[idx2] == target:
                result.append(idx1 + 1)
                result.append(idx2 + 1)
                break
            elif numbers[idx1] + numbers[idx2] < target:
                idx1 += 1
            elif numbers[idx1] + numbers[idx2] > target:
                idx2 -= 1

        return result