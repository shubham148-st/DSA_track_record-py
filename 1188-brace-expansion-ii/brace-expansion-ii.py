class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        def parse(s: str) -> set[str]:
            parts = []
            depth = 0
            start = 0
            for i, char in enumerate(s):
                if char == '{':
                    depth += 1
                elif char == '}':
                    depth -= 1
                elif char == ',' and depth == 0:
                    parts.append(s[start:i])
                    start = i + 1
            parts.append(s[start:])

            if len(parts) > 1:
                result = set()
                for p in parts:
                    result.update(parse(p))
                return result

            factors = []
            i = 0
            n = len(s)
            while i < n:
                if s[i] == '{':
                    j = i
                    d = 0
                    while j < n:
                        if s[j] == '{':
                            d += 1
                        elif s[j] == '}':
                            d -= 1
                        if d == 0:
                            break
                        j += 1
                    inner = s[i + 1:j]
                    factors.append(parse(inner))
                    i = j + 1
                else:
                    j = i
                    while j < n and s[j] != '{':
                        j += 1
                    word = s[i:j]
                    factors.append({word})
                    i = j

            current = {""}
            for factor in factors:
                next_set = set()
                for prefix in current:
                    for word in factor:
                        next_set.add(prefix + word)
                current = next_set
            return current

        return sorted(list(parse(expression)))