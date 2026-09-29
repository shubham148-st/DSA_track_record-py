class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        m = len(grid)
        n = len(grid[0])
        
        if (m + n) % 2 == 0:
            return False
        
        if grid[0][0] == ')' or grid[m - 1][n - 1] == '(':
            return False
            
        dp = [[set() for _ in range(n)] for _ in range(m)]
        dp[0][0].add(1)
        
        for r in range(m):
            for c in range(n):
                if r == 0 and c == 0:
                    continue
                
                val = 1 if grid[r][c] == '(' else -1
                prev_balances = set()
                
                if r > 0:
                    prev_balances.update(dp[r - 1][c])
                if c > 0:
                    prev_balances.update(dp[r][c - 1])
                    
                for b in prev_balances:
                    nb = b + val
                    if nb >= 0:
                        dp[r][c].add(nb)
                        
        return 0 in dp[m - 1][n - 1]