class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        arr2.sort()
        count = 0
        
        import bisect
        for x in arr1:
            idx = bisect.bisect_left(arr2, x)
            valid = True
            
            if idx < len(arr2) and abs(arr2[idx] - x) <= d:
                valid = False
            if idx > 0 and abs(arr2[idx - 1] - x) <= d:
                valid = False
                
            if valid:
                count += 1
                
        return count