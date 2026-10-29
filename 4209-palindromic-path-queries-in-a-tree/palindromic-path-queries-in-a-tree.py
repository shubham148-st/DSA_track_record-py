class Solution:
    def palindromePath(self, n: int, edges: list[list[int]], s: str, queries: list[str]) -> list[bool]:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            
        parent = [-1] * n
        depth = [0] * n
        heavy = [-1] * n
        head = [0] * n
        pos = [0] * n
        
        def dfs1(u, p, d):
            parent[u] = p
            depth[u] = d
            size = 1
            max_sub_size = 0
            for v in adj[u]:
                if v != p:
                    sub_size = dfs1(v, u, d + 1)
                    size += sub_size
                    if sub_size > max_sub_size:
                        max_sub_size = sub_size
                        heavy[u] = v
            return size

        cur_pos = 0
        def dfs2(u, h):
            nonlocal cur_pos
            head[u] = h
            pos[u] = cur_pos
            cur_pos += 1
            if heavy[u] != -1:
                dfs2(heavy[u], h)
            for v in adj[u]:
                if v != parent[u] and v != heavy[u]:
                    dfs2(v, v)
                    
        dfs1(0, -1, 0)
        dfs2(0, 0)
        
        tree_mask = [0] * (4 * n)
        
        def update_seg(node, l, r, idx, val):
            if l == r:
                tree_mask[node] = val
                return
            mid = (l + r) // 2
            if idx <= mid:
                update_seg(2 * node, l, mid, idx, val)
            else:
                update_seg(2 * node + 1, mid + 1, r, idx, val)
            tree_mask[node] = tree_mask[2 * node] ^ tree_mask[2 * node + 1]

        def query_seg(node, l, r, ql, qr):
            if ql > r or qr < l:
                return 0
            if ql <= l and r <= qr:
                return tree_mask[node]
            mid = (l + r) // 2
            return query_seg(2 * node, l, mid, ql, qr) ^ query_seg(2 * node + 1, mid + 1, r, ql, qr)

        def query_path(u, v):
            res = 0
            while head[u] != head[v]:
                if depth[head[u]] > depth[head[v]]:
                    u, v = v, u
                res ^= query_seg(1, 0, n - 1, pos[head[v]], pos[v])
                v = parent[head[v]]
            if depth[u] > depth[v]:
                u, v = v, u
            res ^= query_seg(1, 0, n - 1, pos[u], pos[v])
            return res

        s_list = list(s)
        for i in range(n):
            update_seg(1, 0, n - 1, pos[i], 1 << (ord(s_list[i]) - ord('a')))
            
        answer = []
        for q in queries:
            parts = q.split()
            if parts[0] == 'update':
                u = int(parts[1])
                c = parts[2]
                s_list[u] = c
                update_seg(1, 0, n - 1, pos[u], 1 << (ord(c) - ord('a')))
            else:
                u, v = int(parts[1]), int(parts[2])
                mask = query_path(u, v)
                answer.append(mask == 0 or (mask & (mask - 1)) == 0)
                
        return answer