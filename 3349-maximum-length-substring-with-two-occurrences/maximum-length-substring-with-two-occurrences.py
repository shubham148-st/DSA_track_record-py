class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        left = 0
        max_length = 0
        char_count = [0] * 26

        for right in range(len(s)):
            char_index = ord(s[right]) - ord("a")
            char_count[char_index] += 1

            while char_count[char_index] > 2:
                char_count[ord(s[left]) - ord("a")] -= 1
                left += 1

            max_length = max(max_length, right - left + 1)

        return max_length
