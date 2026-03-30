class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_count = 1
        i, j = 0, 0
        if len(s) == 0:
            return 0

        string_map = {s[i]: i}

        while j < len(s) - 1:
            j = j + 1
            if s[j] not in string_map:
                max_count = max(max_count, j - i + 1)
                string_map[s[j]] = j
            else:
                i= string_map[s[i]] + 1
                j = i
                string_map.clear()
                string_map[s[i]] = i 
        return max_count


        