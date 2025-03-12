class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for tok in tokens:
            if tok == "+":
                x = stack.pop()
                y = stack.pop()
                stack.append(x+y)
            
            elif tok == "-":
                x = stack.pop()
                y = stack.pop()
                stack.append(y-x)
                
            elif tok == "*":
                x = stack.pop()
                y = stack.pop()
                stack.append(x*y)
                
            elif tok == "/":
                x = stack.pop()
                y = stack.pop()
                stack.append(int(y/x))
            else:
                stack.append(int(tok))
        return stack[-1]