class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        m = len(queries)
        ans = [0] * m
        logs.sort(key=lambda l: l[1])
        
        indexed_queries = sorted(enumerate(queries), key=lambda q: q[1])
        
        log_idx_left = 0
        log_idx_right = 0
        num_logs = len(logs)
        server_counts = [0] * (n + 1)
        active_servers = 0
        
        for orig_idx, q in indexed_queries:
            window_start = q - x
            window_end = q
            
            while log_idx_right < num_logs and logs[log_idx_right][1] <= window_end:
                server = logs[log_idx_right][0]
                if server_counts[server] == 0:
                    active_servers += 1
                server_counts[server] += 1
                log_idx_right += 1
            
            while log_idx_left < num_logs and logs[log_idx_left][1] < window_start:
                server = logs[log_idx_left][0]
                server_counts[server] -= 1
                if server_counts[server] == 0:
                    active_servers -= 1
                log_idx_left += 1
            
            ans[orig_idx] = n - active_servers
            
        return ans