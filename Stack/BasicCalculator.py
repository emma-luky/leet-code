class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        ans = 0
        curr = 0
        sign = 1
        
        for char in s:
            if char.isdigit():
                curr = curr * 10 + int(char)
            elif char == '+':
                ans += curr * sign
                curr = 0
                sign = 1
            elif char == '-':
                ans += curr * sign
                curr = 0
                sign = -1
            elif char == '(':
                stack.append(ans)
                stack.append(sign)
                ans = 0
                sign = 1
            elif char == ')':
                ans += curr * sign
                curr = 0
                ans *= stack.pop()
                ans += stack.pop()
        ans += curr * sign
        return ans
