class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # find the row in which target is stored
        top, bottom = 0, len(matrix) - 1
        while top <= bottom:
            row = (top + bottom) // 2
            if target < matrix[row][0]:
                bottom = row - 1
            elif target > matrix[row][-1]:
                top = row + 1
            else:
                break

        # use the last valid row
        if row < 0:
            row += 1
        elif row > len(matrix):
            row -= 1

        # run binary search on that row
        l, r = 0, len(matrix[0]) - 1
        while l <= r:
            midCol = (l + r) // 2
            if matrix[row][midCol] < target:
                l = midCol + 1
            elif matrix[row][midCol] > target:
                r = midCol - 1
            else:
                return True

        return False