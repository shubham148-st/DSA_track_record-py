class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 10**9 + 7
        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1
        
        last = [-1] * 26
        
        for i in range(1, n + 1):
            x = ord(s[i - 1]) - ord('a')
            dp[i] = (2 * dp[i - 1]) % MOD
            
            if last[x] != -1:
                dp[i] = (dp[i] - dp[last[x] - 1] + MOD) % MOD
            
            last[x] = i
            
        return (dp[n] - 1 + MOD) % MOD