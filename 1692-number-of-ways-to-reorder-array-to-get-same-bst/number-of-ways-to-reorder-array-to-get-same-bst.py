class Solution:
    def numOfWays(self, nums: list[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        
        table = [[1] * (i + 1) for i in range(n + 1)]
        for i in range(2, n + 1):
            for j in range(1, i):
                table[i][j] = (table[i - 1][j - 1] + table[i - 1][j]) % MOD
                
        def dfs(arr):
            if len(arr) <= 2:
                return 1
            root = arr[0]
            left = [x for x in arr[1:] if x < root]
            right = [x for x in arr[1:] if x > root]
            
            left_ways = dfs(left)
            right_ways = dfs(right)
            
            res = (table[len(left) + len(right)][len(left)] * left_ways) % MOD
            res = (res * right_ways) % MOD
            return res
            
        return (dfs(nums) - 1) % MOD