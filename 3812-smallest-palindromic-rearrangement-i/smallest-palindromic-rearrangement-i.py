class Solution:
    def smallestPalindrome(self, s: str) -> str:
        n = len(s)
        half_len = n // 2
        first_half = "".join(sorted(s[:half_len]))
        mid = s[half_len] if n % 2 == 1 else ""
        return first_half + mid + first_half[::-1]