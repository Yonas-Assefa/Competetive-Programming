class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        arr = [0] * n
        ans = ""

        for left, right, shift in shifts:
            if shift == 0:
                arr[left] -= 1
                if (right + 1) < n:
                    arr[right + 1] += 1
            else:
                arr[left] += 1
                if (right + 1) < n:
                    arr[right + 1] -= 1
        for i in range(1, n):
            arr[i] = arr[i - 1] + arr[i]
        
        for i in range(n):
            char = s[i]
            char_ord = ord(char)
            shift = arr[i] % 26
            
            val = char_ord + shift
            if val < 97:
                val = 122 - (97 - val) + 1
            elif val > 122:
                val = 97 + (val - 122) - 1
                
            ans += chr(val)

        return ans
