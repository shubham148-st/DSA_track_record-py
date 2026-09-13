class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)
        list1 = [(r, c) for r in range(n) for c in range(n) if img1[r][c] == 1]
        list2 = [(r, c) for r in range(n) for c in range(n) if img2[r][c] == 1]
        
        counts = {}
        best_overlap = 0
        
        for p1 in list1:
            for p2 in list2:
                shift_key = (p1[0] - p2[0], p1[1] - p2[1])
                counts[shift_key] = counts.get(shift_key, 0) + 1
                best_overlap = max(best_overlap, counts[shift_key])
                
        return best_overlap