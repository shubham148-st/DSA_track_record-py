class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)
        if s == "".join(sorted(s)):
            return 0
        if n == 2:
            return -1
            
        min_c = s.index(min(s))
        # Find the latest occurrence of the maximum character
        max_c = n - 1 - s[::-1].index(max(s))
        
        if min_c == 0 or max_c == n - 1:
            return 1
        if min_c == n - 1 and max_c == 0:
            return 3
        return 2