class Solution:
    def isValid(self, s: str) -> bool:
        # edge case
        if len(s) == 1:
            return False

        stack: List[str] = []
        isValid: bool = True

        for c in s:
            if c == '(' or c == '[' or c == '{':
                stack.append(c)
                continue
            
            if len(stack) == 0:
                isValid = False
                break

            top: str = stack[-1]
            if (top == '(' and c == ')') or (top == '[' and c == ']') or (top == '{' and c == '}'):
                stack.pop()
            else:
                isValid = False
                break

        if len(stack) > 0:
            isValid = False

        return isValid
