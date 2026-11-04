class Solution:
    def minOperations(self, nums: list[int], x: int, k: int) -> int:
        n = len(nums)
        lower = SortedList()
        upper = SortedList()
        lower_sum = 0
        upper_sum = 0
        
        min_ops = []
        
        for i in range(n):
            val = nums[i]
            if not lower or val <= lower[-1]:
                lower.add(val)
                lower_sum += val
            else:
                upper.add(val)
                upper_sum += val
                
            if i >= x:
                out_num = nums[i - x]
                if out_num in lower:
                    lower.remove(out_num)
                    lower_sum -= out_num
                else:
                    upper.remove(out_num)
                    upper_sum -= out_num
                    
            if len(lower) < len(upper):
                v = upper.pop(0)
                lower.add(v)
                upper_sum -= v
                lower_sum += v
            elif len(lower) - len(upper) > 1:
                v = lower.pop()
                upper.add(v)
                lower_sum -= v
                upper_sum += v
                
            if i >= x - 1:
                median = lower[-1]
                ops = (median * len(lower) - lower_sum) + (upper_sum - median * len(upper))
                min_ops.append(ops)
                
        m = len(min_ops)
        dp = [[float('inf')] * (m + 1) for _ in range(k + 1)]
        for i in range(m + 1):
            dp[0][i] = 0
            
        for j in range(1, k + 1):
            min_prev = float('inf')
            for i in range(1, m + 1):
                min_prev = min(min_prev, dp[j - 1][max(0, i - x)])
                dp[j][i] = min(dp[j][i - 1], min_prev + min_ops[i - 1])
                
        return dp[k][m]