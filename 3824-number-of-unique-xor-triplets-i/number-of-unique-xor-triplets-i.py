import math

class Solution:
    def uniqueXorTriplets(self, nums: list[int]) -> int:
        n = len(nums)
        
        # Base cases for small input lengths
        if n < 3:
            return n
        
        # Calculate the number of bits needed to represent n
        bit_length = n.bit_length()
        
        # Total unique values = 2^bit_length
        return 1 << bit_length