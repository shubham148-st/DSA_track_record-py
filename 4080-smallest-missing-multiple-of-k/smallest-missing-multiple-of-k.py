class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        num_set = set(nums)
        i = 1
        while True:
            x = k * i
            if x not in num_set:
                return x
            i += 1