class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [0] * len(temperatures)
        diffStack = []

        for i, t in enumerate(temperatures):
            while diffStack and t > temperatures[diffStack[-1]]:
                prev_idx = diffStack.pop()
                stack[prev_idx] = i - prev_idx
            
            diffStack.append(i)

        return stack

        
