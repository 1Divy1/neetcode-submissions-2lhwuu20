class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1:
            return int(tokens[0])

        operators: List[str] = ["+", "-", "*", "/"]
        stack: List[str] = []
        result: int = 0

        for item in tokens:
            if item not in operators:
                stack.append(item)
                continue

            operand1: int = stack.pop()
            if len(stack) > 0:
                operand2 = stack.pop()

            match item:
                case "+":
                    result = int(operand2) + int(operand1)
                case "-":
                    result = int(operand2) - int(operand1)
                case "*":
                    result = int(operand2) * int(operand1)
                case "/":  
                    result = int(int(operand2) / int(operand1))
            stack.append(result)

        return result