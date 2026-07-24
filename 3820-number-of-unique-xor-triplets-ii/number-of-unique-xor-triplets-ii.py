class Solution:
    def uniqueXorTriplets(self, nums: list[int]) -> int:
        unique_nums = list(set(nums))
        
        # S2: Pair XORs
        s2 = [False] * 2048
        n = len(unique_nums)
        for i in range(n):
            for j in range(i, n):
                s2[unique_nums[i] ^ unique_nums[j]] = True
                
        # Extract present values from S2
        s2_vals = [val for val in range(2048) if s2[val]]
        
        # S3: Triplet XORs
        s3 = [False] * 2048
        for p in s2_vals:
            for z in unique_nums:
                s3[p ^ z] = True
                
        return sum(s3)