class Solution:
    def minInsertions(self, s: str) -> int:
        open_brackets = 0
        ans = 0
        i = 0
        n = len(s)
        
        while i < n:
            if s[i] == '(':
                open_brackets += 1
                i += 1
            else:
                if i + 1 < n and s[i + 1] == ')':
                    i += 2
                else:
                    ans += 1
                    i += 1
                
                if open_brackets > 0:
                    open_brackets -= 1
                else:
                    ans += 1
                    
        return ans + open_brackets * 2