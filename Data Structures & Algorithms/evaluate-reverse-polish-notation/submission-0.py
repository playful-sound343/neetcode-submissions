class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]

        for token in tokens:
            if token not in '+-*/':
                stack.append(int(token))

            else:
                a=stack.pop()
                b=stack.pop()

                if token=='+':
                    stack.append(a+b)
                elif token=='-':
                    stack.append(a-b)
                elif token=='*':
                    stack.append(a*b)
                elif token=='/':
                    if b!=0:
                        stack.append(int(a/b))

        return stack[0]
                    
            

        