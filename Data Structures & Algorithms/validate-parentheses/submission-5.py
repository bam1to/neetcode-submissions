class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        valid = {'{': '}', '[': ']', '(': ')'}

        for char in s:
            if char in valid:
                stack.append(char)
            else:
                if not stack:
                    return False

                prev = stack.pop()
                if not valid[prev] or valid[prev] != char:
                    return False

        return len(stack) == 0