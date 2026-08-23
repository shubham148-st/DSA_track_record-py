class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        ans = 0.0
        
        for i in range(n // 2):
            ans += 4.5 if num[i] == '?' else int(num[i])
            
        for i in range(n // 2, n):
            ans -= 4.5 if num[i] == '?' else int(num[i])
            
        return ans != 0.0