class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        dp = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            take = 0
            max_diff = -float("inf")

            for k in range(1, 4):
                if i + k <= n:
                    take += stoneValue[i + k - 1]
                    max_diff = max(max_diff, take - dp[i + k])
                else:
                    break
            dp[i] = max_diff

        if dp[0] > 0:
            return "Alice"
        elif dp[0] < 0:
            return "Bob"
        else:
            return "Tie"
