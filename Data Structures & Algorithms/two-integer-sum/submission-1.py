class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pair: List[int] = []

        # create the hashmap [value, index]
        hashmap: dict[int, int] = {}
        for i in range(len(nums)):
            hashmap[nums[i]] = i

        for i in range(len(nums)):
            diff: int = target - nums[i]
            if diff in hashmap and i != hashmap.get(diff):
                if i < hashmap.get(diff):
                    pair = [i, hashmap.get(diff)]
                else:
                    pair = [hashmap.get(diff), i]
                break

        return pair
