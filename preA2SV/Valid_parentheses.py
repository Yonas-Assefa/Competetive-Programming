class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)% 2!= 0:
            return False
        stack=[]
        para_dict={'(' : ')', '[' : ']', '{' : '}'}
        for i in s:
            if i in para_dict.keys():
                stack.append(i)
            elif i in para_dict.values():
                if stack==[]:
                    return False
                tag=stack.pop()
                if i != para_dict[tag]:
                    return False
            else:
                return False
        return stack==[]
