class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_count = 1
        i, j = 0, 0
        if len(s) == 0:
            return 0

        string_map = {s[i]: i}

        while j < len(s) - 1:
            j = j + 1
            if s[j] in string_map:
                i = max(i, string_map[s[j]] + 1)
            string_map[s[j]] = j
            max_count = max(max_count, j - i + 1)
        return max_count


        