class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        memo = {}

        def solve(left: int, right: int) -> int:
            if left == right:
                return nums[left]
            if (left, right) in memo:
                return memo[(left, right)]
            pick_left = nums[left] - solve(left + 1, right)
            pick_right = nums[right] - solve(left, right - 1)
            memo[(left, right)] = max(pick_left, pick_right)
            return memo[(left, right)]

        return solve(0, len(nums) - 1) >= 0
