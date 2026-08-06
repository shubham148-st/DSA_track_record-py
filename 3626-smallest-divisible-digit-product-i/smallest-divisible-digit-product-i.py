class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        i = n
        while True:
            temp = i
            product = 1
            has_zero = False
            
            while temp > 0:
                digit = temp % 10
                if digit == 0:
                    has_zero = True
                    break
                product *= digit
                temp //= 10
            
            if has_zero or product % t == 0:
                return i
            
            i += 1