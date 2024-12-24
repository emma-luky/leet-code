class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for char in s:
            if char == '(' or char == '[' or char == '{':
                stack.append(char)
            else:
                if len(stack) != 0:
                    c = stack.pop()
                    if c == '(' and char == ')':
                        continue
                    elif c == '['and char == ']':
                        continue
                    elif c == '{' and char == '}':
                        continue
                    else:
                        return False
                else:
                    return False
        if len(stack) == 0:
            return True
        else:
            return False
