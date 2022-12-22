class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        alphabet_order = {}
        no_of_words = len(words)

        for index, char in enumerate(order):
            alphabet_order[char] = index
        
        for i in range(no_of_words - 1):
            if not self.compare_two_words(alphabet_order, words[i], words[i + 1]):
                return False
        return True
    
    def compare_two_words(self, alphabet_order, word1, word2):
        char = 0
        word1_len = len(word1)
        word2_len = len(word2)

        while (char < word1_len and
                    char < word2_len):
                if alphabet_order[word1[char]] < alphabet_order[word2[char]]:
                        return True
                if alphabet_order[word1[char]] > alphabet_order[word2[char]]:
                        return False
                char += 1

        if word1_len > char:
            return False
        return True
        
        
                
                        

            