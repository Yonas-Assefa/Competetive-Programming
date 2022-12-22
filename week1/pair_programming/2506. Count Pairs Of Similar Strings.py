class Solution:
    def similarPairs(self, words: List[str]) -> int:
        # wordCountSet = []
        # for i in words:
        #     count = {}
        #     for j in i:
        #         count[j] = count.get(j, 0) + 1
        #     wordCountSet.append(set(count.keys()))
        # count = 0
        # print(wordCountSet)
        # for i in range(len(wordCountSet)):
        #     for j in range(i+1,len(wordCountSet)):
        #         if i != j:
        #             if wordCountSet[i] == wordCountSet[j]:
        #                 count += 1
                        
        # return count
        n = len(words)
        count = 0
        for i in range(n):
            for j in range(i+1, n):
                if set(words[i]) == set(words[j]):
                    count += 1
        return count

        