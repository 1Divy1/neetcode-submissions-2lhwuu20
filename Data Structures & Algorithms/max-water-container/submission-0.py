class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        area: int = 0

        while l < r:
            tempArea: int = (r - l) * min(heights[l], heights[r])

            if tempArea > area:
                area = tempArea
            
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return area
