class Solution:
    def isValid(self, s: str) -> bool:
        opening_set = {"(", "[", "{"}
        closing_pairs = {")": "(", "]":"[", "}":"{"}
        brackets = []
        for i in s:
            if i in opening_set:
                brackets.append(i)
            if i in closing_pairs:
                if brackets != [] and brackets[-1] == closing_pairs[i]:
                    brackets.pop()
                else:
                    return False
        
        return brackets == []