class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        right = [0] * n
        right[n - 1] = nums[n - 1]

        for i in range(n - 2, -1, -1):
            right[i] = min(right[i + 1], nums[i])

        left_max = 0
        for i in range(n):
            left_max = max(left_max, nums[i])
            if left_max - right[i] <= k:
                return i

        return -1
