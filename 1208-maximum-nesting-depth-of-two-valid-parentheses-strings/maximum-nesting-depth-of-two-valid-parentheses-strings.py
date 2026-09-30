class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        result = []
        depth = 0
        
        for c in seq:
            if c == '(':
                result.append(depth % 2)
                depth += 1
            else:
                depth -= 1
                result.append(depth % 2)
                
        return result