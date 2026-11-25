class Solution:
    def smallestUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        BASE = 1315423911
        MOD = 10**9 + 7

        pow_base = [1] * (n + 1)
        for i in range(1, n + 1):
            pow_base[i] = (pow_base[i - 1] * BASE) % MOD

        def has_unique_of_len(length: int) -> bool:
            h = 0
            for i in range(length):
                h = (h * BASE + nums[i]) % MOD

            freq = Counter([h])
            for i in range(length, n):
                out_val = (nums[i - length] * pow_base[length - 1]) % MOD
                h = (h - out_val) % MOD
                h = (h * BASE + nums[i]) % MOD
                freq[h] += 1

            return any(count == 1 for count in freq.values())

        lo, hi = 1, n
        ans = n
        while lo <= hi:
            mid = (lo + hi) // 2
            if has_unique_of_len(mid):
                ans = mid
                hi = mid - 1
            else:
                lo = mid + 1
        return ans