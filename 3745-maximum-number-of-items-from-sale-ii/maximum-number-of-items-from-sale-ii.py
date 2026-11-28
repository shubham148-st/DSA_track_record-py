class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)
        cnt_factor = [0] * (n + 1)
        for factor, _ in items:
            cnt_factor[factor] += 1

        mult_sum = [0] * (n + 1)
        for f in range(1, n + 1):
            total = 0
            for m in range(f, n + 1, f):
                total += cnt_factor[m]
            mult_sum[f] = total

        # Each deal: (gain, cost, max_cnt)
        deals = []
        inf = 10**18
        for factor, price in items:
            bonus = max(0, mult_sum[factor] - 1)
            if bonus > 0:
                deals.append((2, price, bonus))
            deals.append((1, price, inf))

        # Sort by gain / cost descending: g1 / c1 > g2 / c2  <=>  g1 * c2 > g2 * c1
        from functools import cmp_to_key
        def cmp_deals(a, b):
            left = a[0] * b[1]
            right = b[0] * a[1]
            if left > right:
                return -1
            if left < right:
                return 1
            return 0

        deals.sort(key=cmp_to_key(cmp_deals))

        rem_budget = budget
        ans = 0
        for gain, cost, max_cnt in deals:
            if rem_budget < cost:
                continue
            take = min(max_cnt, rem_budget // cost)
            ans += take * gain
            rem_budget -= take * cost

        return ans