class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_count = 1
        i, j = 0, 0
        if len(s) == 0:
            return 0
        string_set = {s[0]}
        while j < len(s) - 1:
            j = j + 1
            if s[j] not in string_set:
                max_count = max(max_count, j - i + 1)
                string_set.add(s[j])
            else:
                string_set.clear()
                while s[i] != s[j]:
                    i = i + 1
                i= i+1
                j = i
                string_set = {s[i]}
        return max_count


        