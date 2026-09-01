class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        if len(s)==1:
            return False
        for i in range(0,len(s)):
            if s[i] in ['[','{','(']:
                stack.append(s[i])
            elif s[i] == ']':
                if len(stack)!=0 and stack[-1] == '[':
                    stack.pop()
                else:
                    stack.append(s[i])
            elif s[i] == '}':
                if len(stack)!=0 and stack[-1] == '{':
                    stack.pop()
                else:
                    stack.append(s[i])
            elif s[i] == ')':
                if len(stack)!=0 and stack[-1] == '(':
                    stack.pop()
                else:
                    stack.append(s[i])
        if len(stack) == 0:
            return True
        else:
            return False


                
        
        