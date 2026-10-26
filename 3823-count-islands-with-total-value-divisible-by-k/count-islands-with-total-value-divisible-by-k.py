class Solution:
    def countIslands(self, grid: list[list[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        count = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] > 0:
                    island_sum = 0
                    q = deque([(i, j)])
                    island_sum += grid[i][j]
                    grid[i][j] = 0
                    
                    while q:
                        r, c = q.popleft()
                        for nr, nc in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                            if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] > 0:
                                island_sum += grid[nr][nc]
                                grid[nr][nc] = 0
                                q.append((nr, nc))
                                
                    if island_sum % k == 0:
                        count += 1
                        
        return count