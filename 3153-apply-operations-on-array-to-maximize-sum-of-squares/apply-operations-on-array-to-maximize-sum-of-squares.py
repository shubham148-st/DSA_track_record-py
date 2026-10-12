class Solution:
    def maxSum(self, nums: list[int], k: int) -> int:
        bit_count = [0] * 31
        for num in nums:
            for i in range(31):
                if (num >> i) & 1:
                    bit_count[i] += 1
        
        ans = 0
        MOD = 10**9 + 7
        
        for _ in range(k):
            current = 0
            for bit in range(30, -1, -1):
                if bit_count[bit] > 0:
                    current |= (1 << bit)
                    bit_count[bit] -= 1
            ans = (ans + current * current) % MOD
            
        return ans