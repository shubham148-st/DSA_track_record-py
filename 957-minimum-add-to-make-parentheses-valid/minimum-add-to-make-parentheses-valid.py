class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        open_brackets = 0
        ans = 0
        for c in s:
            if c == '(':
                open_brackets += 1
            else:
                if open_brackets > 0:
                    open_brackets -= 1
                else:
                    ans += 1
        return ans + open_brackets