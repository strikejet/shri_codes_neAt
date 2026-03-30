class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        sorted_strs = sorted(strs,key=len)
        first = sorted_strs[0]
        prefix_len = 0        
        for i in range(len(first)):
            ch = first[i]
            for s in sorted_strs[1:]:
                if s[i] != ch:
                    return first[:prefix_len]
            prefix_len += 1

        return first