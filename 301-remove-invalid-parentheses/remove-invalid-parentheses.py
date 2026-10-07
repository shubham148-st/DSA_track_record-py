class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        if not s:
            return [""]
        
        def is_valid(string: str) -> bool:
            count = 0
            for char in string:
                if char == '(':
                    count += 1
                elif char == ')':
                    count -= 1
                if count < 0:
                    return False
            return count == 0

        visited = {s}
        queue = deque([s])
        result = []
        found = False

        while queue:
            level_size = len(queue)
            current_level_res = []

            for _ in range(level_size):
                curr = queue.popleft()

                if is_valid(curr):
                    current_level_res.append(curr)
                    found = True

                if found:
                    continue

                for i in range(len(curr)):
                    if curr[i] not in ('(', ')'):
                        continue
                    nxt = curr[:i] + curr[i+1:]
                    if nxt not in visited:
                        visited.add(nxt)
                        queue.append(nxt)

            if found:
                return list(set(current_level_res))

        return [""]