class Solution:
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:
        busy = [] # stores (end_time, server_id)
        available = list(range(k)) # stores available server IDs
        request_count = [0] * k
        
        for i, (curr_time, l) in enumerate(zip(arrival, load)):
            end_time = curr_time + l
            
            # Free up servers whose tasks have finished by curr_time
            while busy and busy[0][0] <= curr_time:
                _, server = heapq.heappop(busy)
                bisect.insort(available, server)
                
            if not available:
                continue
                
            preferred = i % k
            idx = bisect.bisect_left(available, preferred)
            if idx == len(available):
                idx = 0
                
            server = available.pop(idx)
            heapq.heappush(busy, (end_time, server))
            request_count[server] += 1
            
        max_requests = max(request_count)
        return [i for i, count in enumerate(request_count) if count == max_requests]