class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for val in asteroids:
            while stack and val < 0 and stack[-1] > 0:
                if stack[-1] < -val:
                    stack.pop()
                    continue
                elif stack[-1] == -val:
                    stack.pop()
                break
            else:
                stack.append(val)
        return stack

        