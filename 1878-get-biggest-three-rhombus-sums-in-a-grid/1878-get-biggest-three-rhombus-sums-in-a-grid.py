from typing import List

class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        # m = number of rows, n = number of columns
        m, n = len(grid), len(grid[0])

        # dr[r][c] will help us get sums along a down-right diagonal (\ direction)
        # We make it 1 row and 1 column bigger to avoid boundary checks.
        dr = [[0] * (n + 1) for _ in range(m + 1)]

        # dl[r][c] will help us get sums along a down-left diagonal (/ direction)
        # We use n+2 columns because the formula refers to j+1.
        dl = [[0] * (n + 2) for _ in range(m + 1)]

        # Build diagonal prefix sums.
        for i in range(m):
            for j in range(n):
                # down-right diagonal prefix:
                # current cell + prefix from top-left neighbor
                dr[i + 1][j + 1] = dr[i][j] + grid[i][j]

                # down-left diagonal prefix:
                # current cell + prefix from top-right neighbor
                dl[i + 1][j] = dl[i][j + 1] + grid[i][j]

        def sum_dr(r1: int, c1: int, r2: int, c2: int) -> int:
            """
            Return sum of cells on the same down-right diagonal
            from (r1, c1) to (r2, c2), inclusive.

            Example direction:
                (r1,c1) -> (r1+1,c1+1) -> ... -> (r2,c2)
            """
            return dr[r2 + 1][c2 + 1] - dr[r1][c1]

        def sum_dl(r1: int, c1: int, r2: int, c2: int) -> int:
            """
            Return sum of cells on the same down-left diagonal
            from (r1, c1) to (r2, c2), inclusive.

            Example direction:
                (r1,c1) -> (r1+1,c1-1) -> ... -> (r2,c2)
            """
            return dl[r2 + 1][c2] - dl[r1][c1 + 1]

        # Use a set so we keep only distinct rhombus sums.
        vals = set()

        # Try every cell as the center of a rhombus.
        for i in range(m):
            for j in range(n):
                # Radius 0 rhombus = just the single cell itself.
                vals.add(grid[i][j])

                # Largest possible radius so that all 4 corners stay inside the grid.
                max_k = min(i, m - 1 - i, j, n - 1 - j)

                # Try every valid rhombus size centered at (i, j).
                for k in range(1, max_k + 1):
                    # The 4 corners of the rhombus
                    top = (i - k, j)
                    right = (i, j + k)
                    bottom = (i + k, j)
                    left = (i, j - k)

                    # Each side of the rhombus lies on a diagonal:
                    #
                    #   top -> right    is down-right
                    #   right -> bottom is down-left
                    #   left -> bottom  is down-right
                    #   top -> left     is down-left

                    s1 = sum_dr(top[0], top[1], right[0], right[1])
                    s2 = sum_dl(right[0], right[1], bottom[0], bottom[1])
                    s3 = sum_dr(left[0], left[1], bottom[0], bottom[1])
                    s4 = sum_dl(top[0], top[1], left[0], left[1])

                    # Adding the 4 edge sums counts each corner twice,
                    # because each corner belongs to two neighboring edges.
                    # So subtract each corner once.
                    total = (
                        s1 + s2 + s3 + s4
                        - grid[top[0]][top[1]]
                        - grid[right[0]][right[1]]
                        - grid[bottom[0]][bottom[1]]
                        - grid[left[0]][left[1]]
                    )

                    vals.add(total)

        # Return the biggest 3 distinct sums in descending order.
        return sorted(vals, reverse=True)[:3]