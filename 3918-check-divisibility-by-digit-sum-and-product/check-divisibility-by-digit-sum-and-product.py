class Solution:
    def checkDivisibility(self, n: int) -> bool:
        digits = [int(c) for c in str(n)]
        digit_sum = sum(digits)
        digit_prod = 1
        for d in digits:
            digit_prod *= d
        total = digit_sum + digit_prod
        return n % total == 0
