class Solution:
    def maxProduct(self, words: List[str]) -> int:
        word_lst = []
        for i in range(len(words)):
            word = words[i]
            char_set = set()
            num = 0
            for j in range(len(word)):
                letr = word[j]
                if letr in char_set:
                    continue

                ltrOrd = ord(letr) - 97
                num += (2 ** ltrOrd)
                char_set.add(letr)

            word_lst.append(num)
        print(words)
        length = 0
        for i in range(len(words)):

            for j in range(i + 1, len(words)):
                if word_lst[i] & word_lst[j] == 0:
                    length = max(length, len(words[i]) * len(words[j]))
        return length
    # def bit_length(self, word1):
    #     count = 0
    #     while word1 > 0:
    #         if word1 % 2 != 0:
    #             count += 1

    #         word1 = word1 >> 1
        
    #     return count



