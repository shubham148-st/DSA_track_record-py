class Solution:
    def countCommas(self, n: int) -> int:
        total_commas = 0
        power_of_10 = 1000
        k = 1
        
        while power_of_10 <= n:
            next_power = power_of_10 * 1000
            upper_bound = min(n, next_power - 1)
            count = upper_bound - power_of_10 + 1
            
            if count > 0:
                total_commas += count * k
                
            power_of_10 = next_power
            k += 1
            
        return total_commas