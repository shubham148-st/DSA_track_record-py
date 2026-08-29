class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        n = len(nums)
        indexed_nums = sorted((val, i) for i, val in enumerate(nums))
        
        groups = []
        for val, i in indexed_nums:
            if not groups or val - groups[-1][-1][0] > limit:
                groups.append([(val, i)])
            else:
                groups[-1].append((val, i))
                
        res = [0] * n
        for group in groups:
            indices = sorted(i for val, i in group)
            for idx, (val, original_i) in zip(indices, group):
                res[idx] = val
                
        return res