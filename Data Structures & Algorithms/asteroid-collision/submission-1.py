class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        def add_stack(val):
            if not stack or val > 0 or stack[-1] < 0:
                stack.append(val)
                return
            
            # collision case: stack[-1] > 0 and val < 0
            if stack[-1] < -val:
                stack.pop()
                add_stack(val)   # keep checking (recursion)
            elif stack[-1] == -val:
                stack.pop()      # both destroyed
            else:
                pass             # incoming destroyed (do nothing)

        for val in asteroids:
            add_stack(val)

        return stack