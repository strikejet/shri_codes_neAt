class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2) or len(s1) == 0:
            return False

        i, j = 0, len(s1)
        c = Counter(s1)
        while j <= len(s2):
            if Counter(s2[i:j]) == c:
                return True
            i = i + 1
            j = j + 1
        return False
