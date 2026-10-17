class Solution:
    def minSwaps(self, nums: list[int]) -> int:
        def get_digit_sum(x):
            s = 0
            while x > 0:
                s += x % 10
                x //= 10
            return s
            
        n = len(nums)
        target = sorted([(get_digit_sum(nums[i]), nums[i]) for i in range(n)])
        pos = {val: idx for idx, (_, val) in enumerate(target)}
        
        vis = [False] * n
        swaps = 0
        
        for i in range(n):
            if not vis[i] and pos[nums[i]] != i:
                cycle_size = 0
                j = i
                while not vis[j]:
                    vis[j] = True
                    j = pos[nums[j]]
                    cycle_size += 1
                swaps += cycle_size - 1
                
        return swaps