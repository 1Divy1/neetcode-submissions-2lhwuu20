class Solution:
    def isValid(self, s: str) -> bool:

        openBrackets = []
        for c in s:
            if c == '{' or c == '[' or c == '(':
                openBrackets.append(c)
            elif c == '}' or c == ']' or c == ')':
                if not openBrackets:
                    return False
                top = openBrackets.pop()
                if not (top == "(" and c == ")") and not (top == "[" and c == "]") and not (top == "{" and c == "}"):
                    return False

        if not openBrackets:
            return True

        return False