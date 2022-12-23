class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        min_len = len(word1) if len(word2) >= len(word1) else len(word2)
        merged_word = ""
        word1_len = len(word1)
        word2_len = len(word2)
        
        for i in range(min_len):
            merged_word += word1[i] + word2[i]
        
        if (len(merged_word) / 2) < word2_len:
            merged_word += word2[word1_len:word2_len]
        elif (len(merged_word) / 2) < word1_len:
            merged_word += word1[word2_len:word1_len]
        return merged_word
        
        