class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i, j = 0, 0 
        hash_map = {}
        max_freq = 0

        ans = 0
        while j < len(s):
            hash_map[s[j]] = hash_map.get(s[j], 0) + 1
            max_freq = max(max_freq, hash_map[s[j]])

            while (j - i + 1) - max_freq > k:
                hash_map[s[i]] -= 1
                i += 1

            ans = max(ans, j - i + 1)
            j += 1


        return ans
            