class Solution:
    def scoreOfParentheses(self, s: str) -> int:
         
        stack = [0]   
        
        for char in s:
            if char == '(':
                stack.append(0)   
            else:
                last = stack.pop()  
                score = max(2 * last, 1)  
                stack[-1] += score   

        return stack[0]  
