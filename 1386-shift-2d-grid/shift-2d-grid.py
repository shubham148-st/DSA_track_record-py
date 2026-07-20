class Solution:
    def shiftGrid(self, grid: list[list[int]], k: int) -> list[list[int]]:
        m, n = len(grid), len(grid[0])
        total_elements = m * n
        
        # Optimize k to avoid redundant full rotations
        k = k % total_elements
        if k == 0:
            return grid
            
        # Initialize a new grid of the same size to store the results
        result = [[0] * n for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                # 1. Convert current 2D coordinates to a 1D index
                old_1d = i * n + j
                
                # 2. Find the new 1D index after shifting
                new_1d = (old_1d + k) % total_elements
                
                # 3. Convert the new 1D index back to 2D coordinates
                new_row = new_1d // n
                new_col = new_1d % n
                
                # Place the element in the result grid
                result[new_row][new_col] = grid[i][j]
                
        return result