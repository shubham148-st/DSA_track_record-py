class Solution:
    def reverseDegree(self, s: str) -> int:
        degree = 0
        for i, char in enumerate(s, start=1):
            reverse_idx = 26 - (ord(char) - ord('a'))
            degree += reverse_idx * i
        return degree