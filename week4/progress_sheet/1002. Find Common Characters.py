class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        from collections import defaultdict

        min_len = float("inf")
        no_words = len(words)
        
        base_word = defaultdict(lambda: 0)
        ans = []

        for word in words:
            if len(word) < min_len:
                min_len = len(word)

                for ltr in word:
                    base_word[ltr] = base_word.get(ltr, 0) + 1
        
        for letter in base_word:
            flag = True

            for i in words:
                temp_dict = defaultdict(lambda: 0)
                
                for j in i:
                    temp_dict[j] = temp_dict.get(j, 0) + 1
                if base_word[letter] != temp_dict[letter]:
                    flag = False
            if flag:
                ans.append(letter)
        return ans

            


        

    