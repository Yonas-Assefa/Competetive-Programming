class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack=[]
        for i in s:
            if i != ")":
                stack.append(i)
            else:
                if stack:
                    st=""
                    temp=stack.pop()
                    while temp!="(":
                        st+=temp
                        temp=stack.pop()
                    for i in st:
                        stack.append(i)
        st=""
        for i in stack:
            st+=i
        return st
                    
        
