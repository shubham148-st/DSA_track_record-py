class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        m, n = len(classroom), len(classroom[0])
        lookup = {}
        r = c = -1
        
        for i in range(m):
            for j in range(n):
                curr = classroom[i][j]
                if curr == 'S':
                    r, c = i, j
                elif curr == 'L':
                    lookup[(i, j)] = len(lookup)
                    
        num_litters = len(lookup)
        if num_litters == 0:
            return 0
            
        target_mask = (1 << num_litters) - 1
        # Track max energy for each cell and mask combination
        # best_energy[r][c][mask] = max energy seen so far
        best_energy = [[[-1] * (1 << num_litters) for _ in range(n)] for _ in range(m)]
        
        q = [(r, c, 0, energy)]  # (r, c, mask, current_energy)
        best_energy[r][c][0] = energy
        
        directions = ((1, 0), (0, 1), (-1, 0), (0, -1))
        moves = 0
        
        while q:
            new_q = []
            for r, c, mask, ne in q:
                if mask == target_mask:
                    return moves
                
                for dr, dc in directions:
                    ni, nj = r + dr, c + dc
                    if not (0 <= ni < m and 0 <= nj < n) or classroom[ni][nj] == 'X':
                        continue
                        
                    n_energy = ne - 1
                    if n_energy < 0:
                        continue
                        
                    new_mask = mask
                    if classroom[ni][nj] == 'R':
                        n_energy = energy
                    elif classroom[ni][nj] == 'L':
                        bit = lookup[(ni, nj)]
                        if not (mask & (1 << bit)):
                            new_mask |= (1 << bit)
                            
                    if n_energy <= best_energy[ni][nj][new_mask]:
                        continue
                        
                    best_energy[ni][nj][new_mask] = n_energy
                    new_q.append((ni, nj, new_mask, n_energy))
                    
            q = new_q
            moves += 1
            
        return -1