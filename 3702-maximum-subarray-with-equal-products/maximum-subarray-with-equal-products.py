class Solution:
    def maxLength(self, nums: List[int]) -> int:
        n = len(nums)
        cnt = 0
        for i in range(n):
            prod = 1
            l = 1
            g = 0
            for j in range(i, n):
                x = nums[j]
                prod *= x
                l = math.lcm(l, x)
                g = math.gcd(g, x)
                product = l * g
                if prod == product:
                    cnt = max(cnt, j - i + 1)
        return cnt
