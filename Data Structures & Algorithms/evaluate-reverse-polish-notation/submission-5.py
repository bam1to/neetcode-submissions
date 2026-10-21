class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for tocken in tokens:
            if tocken.lstrip("+-").isdigit():
                stack.append(int(tocken))
            else:
                firstNum = stack.pop()
                secondNum = stack.pop()

                summ = self.calculate(firstNum, secondNum, tocken)
                stack.append(int(summ))

        return math.floor(stack[-1])

    def calculate(self, firstInt: int, secondInt: int, operand: str) -> int:
        match operand:
            case '+':
                return secondInt + firstInt
            case '-':
                return secondInt - firstInt
            case '*':
                return secondInt * firstInt
            case '/':
                return secondInt / firstInt

