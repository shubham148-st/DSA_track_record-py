class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        grid = [['#' for _ in range(n)] for _ in range(m)]
        
        # Make the top row free
        for j in range(n):
            grid[0][j] = '.'
            
        # Make the rightmost column free
        for i in range(m):
            grid[i][n - 1] = '.'
            
        return ["".join(row) for row in grid]