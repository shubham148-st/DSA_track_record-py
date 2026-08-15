class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        n = len(nums)
        total_xor = 0
        has_nonzero = False
        
        for x in nums:
            total_xor ^= x
            if x != 0:
                has_nonzero = True
                
        if not has_nonzero:
            return 0
            
        if total_xor != 0:
            return n
            
        return n - 1