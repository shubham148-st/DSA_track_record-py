class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        n = len(nums)

        if k == n:
            return max(nums)

        count = collections.Counter(nums)
        if k == 1:
            return max([num for num in nums if count[num] == 1], default=-1)

        ans = -1
        if count[nums[0]] == 1:
            ans = max(ans, nums[0])
        if count[nums[-1]] == 1:
            ans = max(ans, nums[-1])

        return ans
