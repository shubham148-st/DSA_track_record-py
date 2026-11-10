class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        
        for i in range(n):
            if dp[i] == float('inf'):
                continue
            for step in range(1, 4):
                j = i + step
                if j <= n:
                    cost = dp[i] + costs[j - 1] + (j - i) ** 2
                    if cost < dp[j]:
                        dp[j] = cost
                        
        return dp[n]