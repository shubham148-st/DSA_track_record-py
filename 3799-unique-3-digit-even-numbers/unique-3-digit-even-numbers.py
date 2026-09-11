class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        unique_nums = set()
        
        for p in permutations(digits, 3):
            if p[0] != 0 and p[2] % 2 == 0:
                unique_nums.add(p[0] * 100 + p[1] * 10 + p[2])
                
        return len(unique_nums)