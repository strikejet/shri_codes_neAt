class Solution:
    def validPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        used = False
        def is_valid(s, i, j):
            while i < j:
                if not s[i].isalnum():
                    i += 1
                elif not s[j].isalnum():
                    j -= 1
                elif s[i].lower() != s[j].lower():
                    return False
                else:
                    i += 1
                    j -= 1
            return True
        while i < j:

            if not s[i].isalnum():
                i += 1

            elif not s[j].isalnum():
                j -= 1

            elif s[i].lower() == s[j].lower():
                i += 1
                j -= 1
            else:
                return is_valid(s, i + 1, j) or is_valid(s, i, j - 1)


        return True