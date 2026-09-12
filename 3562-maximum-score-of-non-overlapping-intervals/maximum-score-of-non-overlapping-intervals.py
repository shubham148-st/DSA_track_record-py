class Solution:
    def maximumWeight(self, intervals: list[list[int]]) -> list[int]:
        indexed_intervals = sorted(
            ((interval[0], interval[1], interval[2], i) for i, interval in enumerate(intervals)),
            key=lambda x: x[0]
        )
        
        n = len(indexed_intervals)
        starts = [item[0] for item in indexed_intervals]

        @lru_cache(None)
        def solve(i: int, quota: int):
            if i == n or quota == 0:
                return 0, ()
            
            skip_weight, skip_indices = solve(i + 1, quota)
            
            l, r, weight, original_index = indexed_intervals[i]
            
            j = bisect.bisect_right(starts, r)
            
            next_weight, next_indices = solve(j, quota - 1)
            pick_weight = weight + next_weight
            pick_indices = tuple(sorted((original_index,) + next_indices))
            
            if pick_weight > skip_weight or (pick_weight == skip_weight and pick_indices < skip_indices):
                return pick_weight, pick_indices
            else:
                return skip_weight, skip_indices

        return list(solve(0, 4)[1])