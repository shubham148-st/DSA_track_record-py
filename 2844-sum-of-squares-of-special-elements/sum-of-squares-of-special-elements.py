class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        n = len(nums)
        total_sum = 0
        
        for i, val in enumerate(nums):
            index = i + 1
            if n % index == 0:
                total_sum += val * val
                
        return total_sum