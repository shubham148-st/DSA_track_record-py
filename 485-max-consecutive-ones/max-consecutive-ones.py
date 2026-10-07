class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        mx = 0
        ctr = 0
        for i in nums:
            if i == 1:
                ctr += 1
                if ctr > mx: mx = ctr
            elif i == 0: ctr = 0
        return mx
        