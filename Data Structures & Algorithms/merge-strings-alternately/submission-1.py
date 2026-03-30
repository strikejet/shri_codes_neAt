class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = j = 0
        s = ""
        while i < len(word1) and i < len(word2):
            s = s + word1[i] + word2[i]
            i = i + 1
            j = j + 1

        if len(word1) < len(word2):
            s= s + word2[i:]

        elif len(word1) > len(word2):
            s= s + word1[j:]
        return s