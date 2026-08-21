class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        def get_lcm(a, b):
            return (a * b) // math.gcd(a, b)
            
        def count(x):
            total = 0
            n = len(coins)
            for mask in range(1, 1 << n):
                lcm_val = 1
                bits = 0
                for i in range(n):
                    if (mask >> i) & 1:
                        bits += 1
                        lcm_val = get_lcm(lcm_val, coins[i])
                        if lcm_val > x:
                            break
                if lcm_val <= x:
                    if bits % 2 == 1:
                        total += x // lcm_val
                    else:
                        total -= x // lcm_val
            return total

        low = 1
        high = min(coins) * k
        ans = high
        
        while low <= high:
            mid = (low + high) // 2
            if count(mid) >= k:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
                
        return ans