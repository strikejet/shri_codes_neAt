class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        mono_stack = []
        result = [0] * len(temperatures)
        cnt = 1
        for i in range(len(temperatures) - 1 , -1, -1):
            while mono_stack and temperatures[mono_stack[-1]] <= temperatures[i]:
                mono_stack.pop()
            
            if mono_stack:
                result[i] = mono_stack[-1] - i
            
            mono_stack.append(i)
        return result
