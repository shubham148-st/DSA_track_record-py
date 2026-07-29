class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        freq = Counter(s)
        half_freq = [0] * 26
        mid = ""
        MAX_K = 10**6 + 7
        for char, count in freq.items():
            idx = ord(char) - ord('a')
            half_freq[idx] = count // 2
            if count % 2 == 1:
                mid = char
        def count_permutations(cnts):
            total = sum(cnts)
            res = 1
            rem = total
            for c in cnts:
                if c > 0:
                    res *= comb(rem, c)
                    if res >= MAX_K:
                        return MAX_K
                    rem -= c
            return res
        if count_permutations(half_freq) < k:
            return ""
        half_len = sum(half_freq)
        left_half = []
        for _ in range(half_len):
            for i in range(26):
                if half_freq[i] == 0:
                    continue
                half_freq[i] -= 1
                ways = count_permutations(half_freq)
                if ways >= k:
                    left_half.append(chr(ord('a') + i))
                    break
                else:
                    k -= ways
                    half_freq[i] += 1
        left_str = "".join(left_half)
        return left_str + mid + left_str[::-1]