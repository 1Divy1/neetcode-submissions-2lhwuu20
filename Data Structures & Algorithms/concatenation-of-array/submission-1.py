class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans: List[int] = []

        # how many times we concatenate
        for i in range(2):
            # add each item from 'nums' to 'ans'
            for item in nums:
                ans.append(item)

        return ans