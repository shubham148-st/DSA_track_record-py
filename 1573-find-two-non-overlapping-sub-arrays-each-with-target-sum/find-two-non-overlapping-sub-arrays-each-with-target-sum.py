class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n = len(arr)
        min_len = [float('inf')] * n
        prefix_sum_map = {0: -1}
        
        current_sum = 0
        ans = float('inf')
        min_so_far = float('inf')
        
        for i in range(n):
            current_sum += arr[i]
            needed_sum = current_sum - target
            
            if needed_sum in prefix_sum_map:
                left = prefix_sum_map[needed_sum] + 1
                right = i
                length = right - left + 1
                
                if left > 0 and min_len[left - 1] != float('inf'):
                    ans = min(ans, min_len[left - 1] + length)
                
                min_so_far = min(min_so_far, length)
            
            min_len[i] = min_so_far
            prefix_sum_map[current_sum] = i
        
        return ans if ans != float('inf') else -1