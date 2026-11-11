class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        def get_cost(x: int) -> int:
            if x < 0:
                x = 0
            if x > max(need1, need2):
                x = max(need1, need2)
            c3 = x * costBoth
            c1 = max(0, need1 - x) * cost1
            c2 = max(0, need2 - x) * cost2
            return c3 + c1 + c2

        candidates = [0, need1, need2, min(need1, need2), max(need1, need2)]
        min_c = min(get_cost(x) for x in candidates)

        low, high = 0, max(need1, need2)
        while high - low > 2:
            m1 = low + (high - low) // 3
            m2 = high - (high - low) // 3
            if get_cost(m1) < get_cost(m2):
                high = m2
            else:
                low = m1

        for x in range(low, high + 1):
            min_c = min(min_c, get_cost(x))

        return min_c