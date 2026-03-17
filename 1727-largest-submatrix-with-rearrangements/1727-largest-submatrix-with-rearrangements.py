from typing import List

class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        # Get the number of rows and columns in the matrix.
        rows = len(matrix)
        cols = len(matrix[0])

        # heights[c] will store the number of consecutive 1s
        # in column c ending at the current row.
        heights = [0] * cols

        # This will keep track of the maximum submatrix area found.
        max_area = 0

        # Process each row one by one.
        for r in range(rows):
            # Update the histogram heights for the current row.
            for c in range(cols):
                # If the current cell is 1, extend the height by 1.
                if matrix[r][c] == 1:
                    heights[c] += 1
                else:
                    # If the current cell is 0, the streak of 1s breaks.
                    heights[c] = 0

            # Since we are allowed to rearrange columns,
            # we sort the heights in descending order.
            # This places taller columns first.
            sorted_heights = sorted(heights, reverse=True)

            # Try every possible width from 1 to cols.
            for width in range(1, cols + 1):
                # If we take the first 'width' columns after sorting,
                # the rectangle height is limited by the shortest column
                # among them, which is sorted_heights[width - 1].
                height = sorted_heights[width - 1]

                # Compute the area of the rectangle with this width and height.
                area = height * width

                # Update the maximum area if this rectangle is larger.
                max_area = max(max_area, area)

        # Return the largest area found.
        return max_area