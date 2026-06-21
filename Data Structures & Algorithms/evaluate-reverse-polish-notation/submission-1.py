class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        def eval(op1, operator, op2):
            if operator == "*":
                return int(op1) * int(op2)
            if operator == "/":
                return int(op1) / int(op2)
            if operator == "+":
                return int(op1) + int(op2)
            if operator == "-":
                return int(op1) - int(op2)
            


        operators = ('+', '-', '*', '/')
        for i in tokens:
            if i not in operators:
                stack.append(i)
            else:
                op2 = stack.pop()
                op1 = stack.pop()
                stack.append(eval(op1, i, op2))
        while stack:
            if len(stack) == 1:
                return int(stack.pop())
