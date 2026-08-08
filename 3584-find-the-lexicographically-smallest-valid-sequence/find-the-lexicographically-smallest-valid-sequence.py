class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:
        n1, n2 = len(word1), len(word2)
        last = [-1] * n2
        
        j = n2 - 1
        for i in range(n1 - 1, -1, -1):
            if j >= 0 and word1[i] == word2[j]:
                last[j] = i
                j -= 1
        
        ans = []
        can_skip = True
        j = 0
        for i in range(n1):
            if j == n2:
                break
            
            if word1[i] == word2[j]:
                ans.append(i)
                j += 1
            elif can_skip and (j == n2 - 1 or i < last[j + 1]):
                can_skip = False
                ans.append(i)
                j += 1
                
        return ans if j == n2 else []