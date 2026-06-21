class Solution:
    def isValid(self, s: str) -> bool:
        def is_open(x):
            if x in ('{', '(', '['):
                return True
            return False
        def is_pair(o, c):
            if o == '{' and c == '}':
                return True
            if o == '[' and c == ']':
                return True
            if o == '(' and c == ')':
                return True
            return False
        stack=[]
        for i in s:
            if is_open(i):
                stack.append(i)
            elif stack:
                print(stack)
                o = stack.pop()
                if not is_pair(o, i):
                    return False
            else:
                return False
        return not bool(stack)



        