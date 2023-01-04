class Solution(object):
    def removeComments(self, source):
    
        ans = []
        multi = False
        code_line = ''

        for line in source:
            current = 0
            line_length = len(line)

            while current < line_length:
                if not multi:
                    if line[current] == '/' and current < line_length - 1 and line[current + 1] == '/':
                        break
                    elif line[current] == '/' and current < line_length - 1 and line[current + 1] == '*':
                        multi = True
                        current += 1
                    else:
                        code_line += line[current]
                else:
                    if line[current] == '*' and current < line_length - 1 and line[current + 1] == '/':
                        multi = False
                        current += 1
                current += 1

            if not multi and code_line:
                ans.append(code_line)
                code_line = '' 
                
        return ans