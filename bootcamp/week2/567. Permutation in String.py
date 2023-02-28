class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):return False
        left, right, dict1 = 0, len(s1), {}
        for i in s1:
            dict1[i] = dict1.get(i, 0) + 1
        dict2 = {}
        for i in s2[left : right]:
            dict2[i] = dict2.get(i, 0) + 1
        while right < len(s2):
            if dict1 == dict2:
                return True
            
            dict2[s2[left]] -= 1
            if dict2[s2[left]] == 0:
                del dict2[s2[left]]
                
            dict2[s2[right]] = dict2.get(s2[right], 0) + 1
            right += 1
            left += 1
        
        return dict1 == dict2
        
            
        