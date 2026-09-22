class Solution:
    def resultArray(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
        n = len(nums)
        tree_prod = [1] * (4 * n)
        tree_count = [[0] * k for _ in range(4 * n)]

        def combine(l_prod, l_count, r_prod, r_count):
            prod = (l_prod * r_prod) % k
            count = list(l_count)
            for i in range(k):
                rem = (i * l_prod) % k
                count[rem] += r_count[i]
            return prod, count

        def build(node, start, end):
            if start == end:
                p = nums[start] % k
                tree_prod[node] = p
                tree_count[node][p] = 1
                return
            mid = (start + end) // 2
            build(2 * node, start, mid)
            build(2 * node + 1, mid + 1, end)
            tree_prod[node], tree_count[node] = combine(
                tree_prod[2 * node], tree_count[2 * node],
                tree_prod[2 * node + 1], tree_count[2 * node + 1]
            )

        def update(node, start, end, idx, val):
            if start == end:
                nums[idx] = val
                p = val % k
                tree_prod[node] = p
                for i in range(k):
                    tree_count[node][i] = 0
                tree_count[node][p] = 1
                return
            mid = (start + end) // 2
            if start <= idx <= mid:
                update(2 * node, start, mid, idx, val)
            else:
                update(2 * node + 1, mid + 1, end, idx, val)
            tree_prod[node], tree_count[node] = combine(
                tree_prod[2 * node], tree_count[2 * node],
                tree_prod[2 * node + 1], tree_count[2 * node + 1]
            )

        def query_tree(node, start, end, l, r):
            if r < start or end < l:
                identity_count = [0] * k
                return 1, identity_count
            if l <= start and end <= r:
                return tree_prod[node], tree_count[node]
            mid = (start + end) // 2
            left_prod, left_count = query_tree(2 * node, start, mid, l, r)
            right_prod, right_count = query_tree(2 * node + 1, mid + 1, end, l, r)
            
            left_in = not (r < start or mid < l)
            right_in = not (r < mid + 1 or end < l)
            if not left_in:
                return right_prod, right_count
            if not right_in:
                return left_prod, left_count
            return combine(left_prod, left_count, right_prod, right_count)

        build(1, 0, n - 1)
        result = []
        for idx, val, start, x in queries:
            if nums[idx] != val:
                update(1, 0, n - 1, idx, val)
            if start >= n:
                result.append(0)
                continue
            _, count = query_tree(1, 0, n - 1, start, n - 1)
            result.append(count[x])

        return result