class Solution:
    def compress(self, chars: List[str]) -> int:
        s=""
        i,j=0,1
        count=1
        while j<=(len(chars)-1):
            if chars[i]==chars[j]:
                count+=1
                i+=1
                j+=1
            else:
                if count>1:
                    s+=(chars[i]+str(count))
                else:
                    s+=chars[i]
                i+=1
                j+=1
                count=1
        if count>1:
            s+=chars[i] + str(count)
        else:
            s+=chars[i]
            
        for i in range(len(chars)):
            chars.pop()
        for i in s:
            chars.append(i)
            
        return len(chars)
                    
