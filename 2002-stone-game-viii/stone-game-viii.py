class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        n = len(stones)
        prefix = list(accumulate(stones))
        
        max_diff = prefix[-1]
        for i in range(n - 3, -1, -1):
            max_diff = max(max_diff, prefix[i + 1] - max_diff)
            
        return max_diff