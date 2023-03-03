class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack=[]
        n=len(tokens)
        for i in tokens:
            if(i=="+" or i=="-" or i=='*' or i=="/"):
                b=stack.pop()
                a=stack.pop()
                if (i=="+"):
                    stack.append(int(a+b))
                if(i=="-"):
                    stack.append(int(a-b))
                if(i=="*"):
                    stack.append(int(a*b))
                if(i=="/"):
                    stack.append(int(a/b))
            else:
                stack.append(int(i))

        return(stack[0])