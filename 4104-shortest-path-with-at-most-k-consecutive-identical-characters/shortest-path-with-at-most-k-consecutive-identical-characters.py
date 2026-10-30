class Solution:
    def shortestPath(self, n: int, edges: list[list[int]], labels: str, k: int) -> int:
        adj = [[] for _ in range(n)]
        for u, v, w in edges:
            adj[u].append((v, w))
            
        start_c = ord(labels[0]) - ord('a')
        if 1 > k:
            return -1
            
        pq = [(0, 0, start_c, 1)]
        dist = {}
        dist[(0, start_c, 1)] = 0
        
        while pq:
            w, u, last_c, cnt = heapq.heappop(pq)
            
            if u == n - 1:
                return w
                
            if w > dist.get((u, last_c, cnt), float('inf')):
                continue
                
            for v, weight in adj[u]:
                next_c = ord(labels[v]) - ord('a')
                next_cnt = cnt + 1 if next_c == last_c else 1
                
                if next_cnt > k:
                    continue
                    
                state = (v, next_c, next_cnt)
                if w + weight < dist.get(state, float('inf')):
                    dist[state] = w + weight
                    heapq.heappush(pq, (w + weight, v, next_c, next_cnt))
                    
        return -1