class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)
        cnt = [0] * 26
        for ch in s:
            cnt[ord(ch) - ord('a')] += 1
        
        key = -1
        for c in range(26):
            if cnt[c] % 2 == 1:
                if n % 2 == 0 or key >= 0:
                    return ""
                key = c
                
        ans = []
        
        def check(c: int) -> bool:
            cnt[c] -= 2
            ans.append(chr(ord('a') + c))
            half = "".join(ans)
            
            # Fill the rest of the half with largest available characters (to make the smallest valid suffix)
            for d in range(25, -1, -1):
                half += chr(ord('a') + d) * (cnt[d] // 2)
                
            tmp = half
            if key >= 0:
                tmp += chr(ord('a') + key)
            tmp += half[::-1]
            
            if tmp > target:
                return True
                
            cnt[c] += 2
            ans.pop()
            return False

        for _ in range(n // 2):
            matched = False
            for c in range(26):
                if cnt[c] >= 2 and check(c):
                    matched = True
                    break
            if not matched:
                return ""
                
        ret = "".join(ans)
        if key >= 0:
            ret += chr(ord('a') + key)
        ret += "".join(reversed(ans))
        
        return ret if ret > target else ""