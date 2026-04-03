class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        arr = []
        operations = {'+', '-', '*', '/'}

        for i in tokens:
            if i not in operations:
                arr.append(int(i))
            else:
                one = arr.pop()
                two = arr.pop()

                if i == "+":
                    arr.append(two + one)
                elif i == "-":
                    arr.append(two - one)
                elif i == "*":
                    arr.append(two * one)
                elif i == "/":
                    arr.append(int(two / one))  # truncate toward 0

        return arr[-1]
        