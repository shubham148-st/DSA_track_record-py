class Solution:
    def minimumPushes(self, word: str) -> int:
        counts = Counter(word)
        sorted_frequencies = sorted(counts.values(), reverse=True)
        total_pushes = 0
        for i, freq in enumerate(sorted_frequencies):
            multiplier = (i // 8) + 1
            total_pushes += freq * multiplier     
        return total_pushes