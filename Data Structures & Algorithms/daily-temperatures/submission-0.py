class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        diffStack = []

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1]['v']:
                diffStack.append({'days': i - stack[-1]['idx'], 'idx': stack[-1]['idx']})
                stack.pop()
            
            stack.append({'days': 0, 'idx': i, 'v': t})

        diffStack = diffStack + stack

        sortedDiffs = sorted(diffStack, key=lambda item: item['idx'])

        return [item['days'] for item in sortedDiffs]

        
