class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        R, C = len(grid), len(grid[0])
        
        def bfs(sr, sc):
            q = deque([(sr, sc)])
            grid[sr][sc] = 1
            while q:
                r, c = q.popleft()
                for nr, nc in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                    if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] == 0:
                        grid[nr][nc] = 1
                        q.append((nr, nc))
                        
        # 1. Flood-fill all 0s connected to the boundary
        for r in range(R):
            for c in range(C):
                if (r == 0 or r == R - 1 or c == 0 or c == C - 1) and grid[r][c] == 0:
                    bfs(r, c)
                    
        # 2. Count remaining closed islands
        count = 0
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 0:
                    count += 1
                    bfs(r, c)
                    
        return count