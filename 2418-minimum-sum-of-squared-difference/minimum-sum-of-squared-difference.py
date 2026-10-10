class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        total_k = k1 + k2
        count = [0] * 100001
        total_diff = 0
        
        for n1, n2 in zip(nums1, nums2):
            diff = abs(n1 - n2)
            count[diff] += 1
            total_diff += diff
            
        if total_diff <= total_k:
            return 0
            
        for i in range(100000, 0, -1):
            if count[i] > 0:
                take = min(total_k, count[i])
                count[i] -= take
                count[i - 1] += take
                total_k -= take
                if total_k == 0:
                    break
                    
        ans = 0
        for i in range(100001):
            if count[i] > 0:
                ans += count[i] * i * i
                
        return ans