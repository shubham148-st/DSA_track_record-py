class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        n = len(s)
        leftmost = [n] * 26
        rightmost = [-1] * 26
        
        for i, c in enumerate(s):
            idx = ord(c) - ord('a')
            leftmost[idx] = min(leftmost[idx], i)
            rightmost[idx] = max(rightmost[idx], i)
        
        def get_new_right(i):
            right = rightmost[ord(s[i]) - ord('a')]
            j = i
            while j <= right:
                c_idx = ord(s[j]) - ord('a')
                if leftmost[c_idx] < i:
                    return -1
                right = max(right, rightmost[c_idx])
                j += 1
            return right

        ans = []
        right = -1
        
        for i, c in enumerate(s):
            idx = ord(c) - ord('a')
            if i == leftmost[idx]:
                new_right = get_new_right(i)
                if new_right == -1:
                    continue
                
                if i <= right and ans:
                    ans[-1] = s[i:new_right + 1]
                else:
                    ans.append(s[i:new_right + 1])
                right = new_right
                
        return ans