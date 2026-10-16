class Solution:
    def sumCounts(self, nums: list[int]) -> int:
        n = len(nums)
        MOD = 10**9 + 7
        
        sum_sq = [0] * (4 * n)
        sum_val = [0] * (4 * n)
        lazy = [0] * (4 * n)
        
        def apply(node, l, r, v):
            length = r - l + 1
            sum_sq[node] = (sum_sq[node] + 2 * v * sum_val[node] + v * v * length) % MOD
            sum_val[node] = (sum_val[node] + v * length) % MOD
            lazy[node] = (lazy[node] + v) % MOD

        def push(node, l, r):
            if lazy[node] != 0:
                mid = (l + r) // 2
                apply(2 * node, l, mid, lazy[node])
                apply(2 * node + 1, mid + 1, r, lazy[node])
                lazy[node] = 0

        def update(node, l, r, ql, qr, v):
            if ql > r or qr < l:
                return
            if ql <= l and r <= qr:
                apply(node, l, r, v)
                return
            push(node, l, r)
            mid = (l + r) // 2
            update(2 * node, l, mid, ql, qr, v)
            update(2 * node + 1, mid + 1, r, ql, qr, v)
            sum_sq[node] = (sum_sq[2 * node] + sum_sq[2 * node + 1]) % MOD
            sum_val[node] = (sum_val[2 * node] + sum_val[2 * node + 1]) % MOD

        last_seen = {}
        ans = 0
        
        for r in range(n):
            l = last_seen[nums[r]] + 1 if nums[r] in last_seen else 0
            update(1, 0, n - 1, l, r, 1)
            last_seen[nums[r]] = r
            ans = (ans + sum_sq[1]) % MOD
            
        return ans