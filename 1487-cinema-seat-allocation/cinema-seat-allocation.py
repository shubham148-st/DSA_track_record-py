class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        reserved = defaultdict(set)
        for row, seat in reservedSeats:
            reserved[row].add(seat)
            
        ans = 0
        for row in reserved:
            seats = reserved[row]
            left = all(s not in seats for s in [2, 3, 4, 5])
            right = all(s not in seats for s in [6, 7, 8, 9])
            middle = all(s not in seats for s in [4, 5, 6, 7])
            
            if left and right:
                ans += 2
            elif left or right or middle:
                ans += 1
                
        ans += 2 * (n - len(reserved))
        return ans