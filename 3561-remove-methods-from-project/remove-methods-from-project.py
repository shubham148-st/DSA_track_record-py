class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        from collections import defaultdict, deque
        graph = defaultdict(list)
        for u, v in invocations:
            graph[u].append(v)

        seen = [False] * n
        q = deque([k])
        seen[k] = True

        while q:
            u = q.popleft()
            for v in graph[u]:
                if not seen[v]:
                    seen[v] = True
                    q.append(v)

        for u in range(n):
            if seen[u]:
                continue
            for v in graph[u]:
                if seen[v]:
                    return list(range(n))

        return [i for i in range(n) if not seen[i]]