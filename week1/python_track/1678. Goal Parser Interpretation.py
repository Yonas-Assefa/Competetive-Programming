class Solution:
    def interpret(self, command: str) -> str:
        leftP = 0
        command_len = len(command)
        ans = ""
        
        while leftP < command_len:
            if command[leftP] == "G":
                ans += "G"
                leftP += 1
            else:
                if command[leftP + 1] == ")":
                    ans += "o"
                    leftP += 2
                else:
                    ans += "al"
                    leftP += 4
        return ans
        
