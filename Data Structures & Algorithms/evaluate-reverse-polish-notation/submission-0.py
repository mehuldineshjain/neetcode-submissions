class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        polishStack = []
        for token in tokens:
            if token in ["+", "-", "*", "/"]:
                right = polishStack.pop()
                left = polishStack.pop()
                result = int(eval(f"{left} {token} {right}"))
                polishStack.append(str(result))
            else:
                polishStack.append(token)
        return int(polishStack[-1])