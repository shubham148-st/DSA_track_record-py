class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        result = []
        level = 0
        for ch in s:
            if ch == '(':
                if level > 0:
                    result.append(ch)
                level += 1
            elif ch == ')':
                level -= 1
                if level > 0:
                    result.append(ch)
        return "".join(result)