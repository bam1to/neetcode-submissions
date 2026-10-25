class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []

        sortedByPos = [list(pair) for pair in sorted(zip(position, speed), reverse=True)]

        for i in sortedByPos:
            stack.append((target - i[0]) / i[1])

            if len(stack) > 1 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)
        