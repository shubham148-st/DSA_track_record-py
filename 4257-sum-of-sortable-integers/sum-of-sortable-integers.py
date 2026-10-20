class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        n = len(nums)
        
        # Precompute prefix max and suffix min for global order check
        pref_max = [0] * n
        curr_max = -1
        for i in range(n):
            curr_max = max(curr_max, nums[i])
            pref_max[i] = curr_max
            
        suff_min = [0] * n
        curr_min = float('inf')
        for i in range(n - 1, -1, -1):
            curr_min = min(curr_min, nums[i])
            suff_min[i] = curr_min
            
        total_sum = 0
        
        for k in range(1, n + 1):
            if n % k != 0:
                continue
                
            valid = True
            # Check global ordering between blocks
            for i in range(k - 1, n - 1, k):
                if pref_max[i] > suff_min[i + 1]:
                    valid = False
                    break
            if not valid:
                continue
                
            # Check each block individually for rotation validity
            for i in range(0, n, k):
                block = nums[i:i+k]
                drops = 0
                for j in range(k):
                    if block[j] > block[(j + 1) % k]:
                        drops += 1
                if drops > 1:
                    valid = False
                    break
                    
            if valid:
                total_sum += k
                
        return total_sum