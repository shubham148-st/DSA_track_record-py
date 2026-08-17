class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        n = len(stoneValue)
        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + stoneValue[i]
            
        def get_sum(i: int, j: int) -> int:
            return prefix_sum[j + 1] - prefix_sum[i]
            
        memo = {}
        
        def dfs(i: int, j: int) -> int:
            if i == j:
                return 0
            if (i, j) in memo:
                return memo[(i, j)]
                
            max_score = 0
            for k in range(i, j):
                left_sum = get_sum(i, k)
                right_sum = get_sum(k + 1, j)
                
                if left_sum < right_sum:
                    if max_score >= left_sum * 2:
                        continue
                    max_score = max(max_score, left_sum + dfs(i, k))
                elif left_sum > right_sum:
                    if max_score >= right_sum * 2:
                        break
                    max_score = max(max_score, right_sum + dfs(k + 1, j))
                else:
                    max_score = max(max_score, left_sum + max(dfs(i, k), dfs(k + 1, j)))
                    
            memo[(i, j)] = max_score
            return max_score
            
        return dfs(0, n - 1)