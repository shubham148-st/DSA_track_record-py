class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        n = len(s)
        s = list(s)
        
        tree = [None] * (4 * n)
        
        def update_node(node, left_child, right_child, l, mid, r):
            lc = tree[left_child]
            rc = tree[right_child]
            
            l_len = lc[0]
            if lc[0] == (mid - l + 1) and lc[3] == rc[3]:
                l_len += rc[0]
                
            r_len = rc[1]
            if rc[1] == (r - mid) and rc[4] == lc[4]:
                r_len += lc[1]
                
            max_len = max(lc[2], rc[2])
            if lc[4] == rc[3]:
                max_len = max(max_len, lc[1] + rc[0])
                
            tree[node] = (l_len, r_len, max_len, lc[3], rc[4])

        def build(node, l, r):
            if l == r:
                tree[node] = (1, 1, 1, s[l], s[l])
                return
            mid = (l + r) // 2
            build(2 * node, l, mid)
            build(2 * node + 1, mid + 1, r)
            update_node(node, 2 * node, 2 * node + 1, l, mid, r)

        def update(node, l, r, idx, ch):
            if l == r:
                s[idx] = ch
                tree[node] = (1, 1, 1, ch, ch)
                return
            mid = (l + r) // 2
            if idx <= mid:
                update(2 * node, l, mid, idx, ch)
            else:
                update(2 * node + 1, mid + 1, r, idx, ch)
            update_node(node, 2 * node, 2 * node + 1, l, mid, r)

        build(1, 0, n - 1)
        
        ans = []
        for ch, idx in zip(queryCharacters, queryIndices):
            update(1, 0, n - 1, idx, ch)
            ans.append(tree[1][2])
            
        return ans