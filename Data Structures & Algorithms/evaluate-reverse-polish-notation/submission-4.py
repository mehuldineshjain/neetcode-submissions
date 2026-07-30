class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        polishStack = []
        for token in tokens:
            if token in ["+", "-", "*", "/"]:
                right = polishStack.pop()
                left = polishStack.pop()
                if token == '+':
                    result = left + right
                elif token == '-':
                    result = left - right
                elif token == '*':
                    result = left * right
                elif token == '/':
                    result = int(left / right)
                # result = int(eval(f"{left} {token} {right}"))
                polishStack.append(result)
            else:
                polishStack.append(int(token))
        return int(polishStack[-1])