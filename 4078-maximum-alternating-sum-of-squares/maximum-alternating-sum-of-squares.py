class Solution:
    def maxAlternatingSum(self, nums: list[int]) -> int:
        squares = [x * x for x in nums]
        squares.sort(reverse=True)
        k = (len(nums) + 1) // 2
        return sum(squares[:k]) - sum(squares[k:])