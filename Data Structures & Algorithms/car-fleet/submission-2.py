class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        l = len(position)

        if target == 0:
            return l

        stack = []
        num = 0

        sortedByPos = [list(pair) for pair in sorted(zip(position, speed), reverse=True)]

        for i in sortedByPos:
            carPath = target - i[0]
            time = carPath / i[1]

            if not stack:
                stack.append(time)
                num += 1
                continue

            if stack[-1] >= time:
                continue

            stack = []
            stack.append(time)
            num += 1

        return num
        