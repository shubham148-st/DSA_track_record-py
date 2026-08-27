class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        n = len(s)
        count = [0] * 26
        for char in s:
            count[ord(char) - ord('a')] += 1
            
        ans = ""
        
        def dfs(idx: int, is_greater: bool, current: list) -> bool:
            nonlocal ans
            if idx == n:
                if is_greater:
                    ans = "".join(current)
                    return True
                return False

            for i in range(26):
                if count[i] == 0:
                    continue

                ch = chr(ord('a') + i)

                if not is_greater and ch < target[idx]:
                    continue

                next_is_greater = is_greater or (ch > target[idx])

                count[i] -= 1
                current.append(ch)

                if dfs(idx + 1, next_is_greater, current):
                    return True

                current.pop()
                count[i] += 1

            return False

        if dfs(0, False, []):
            return ans
        return ""