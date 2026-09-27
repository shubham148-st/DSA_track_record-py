class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        current = []

        for char in s:
            if char == "(":
                stack.append(current)
                current = []
            elif char == ")":
                current.reverse()
                if stack:
                    current = stack.pop() + current
            else:
                current.append(char)

        return "".join(current)
