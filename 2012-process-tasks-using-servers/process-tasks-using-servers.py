class Solution:
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:
        free_servers = [(servers[i], i) for i in range(len(servers))]
        heapq.heapify(free_servers)
        
        busy_servers = []
        ans = []
        current_time = 0
        
        for j, task in enumerate(tasks):
            current_time = max(current_time, j)
            
            while busy_servers and busy_servers[0][0] <= current_time:
                _, weight, index = heapq.heappop(busy_servers)
                heapq.heappush(free_servers, (weight, index))
                
            if not free_servers:
                current_time = busy_servers[0][0]
                while busy_servers and busy_servers[0][0] <= current_time:
                    _, weight, index = heapq.heappop(busy_servers)
                    heapq.heappush(free_servers, (weight, index))
                    
            weight, index = heapq.heappop(free_servers)
            ans.append(index)
            heapq.heappush(busy_servers, (current_time + task, weight, index))
            
        return ans