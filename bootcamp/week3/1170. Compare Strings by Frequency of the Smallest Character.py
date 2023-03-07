class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        def charFreq(word):
            
            sorted_word = ''.join(sorted(word))
            smallest_char = sorted_word[0]
            count = 0
            
            for i in sorted_word:
                if i == smallest_char:
                    count += 1
                else:
                    break
            return count
        
        def binarySearch(freq,words):
            left = 0
            right = len(words) - 1
            
            while left < right:
                mid = left + (right - left) // 2
                if words[mid] <= freq:
                    left = mid + 1
                else:
                    right = mid
                    
            return left
        
        for i in range(len(queries)):
            
            query = queries[i]
            query_freq = charFreq(query)
            # print(query_freq)
            queries[i] = query_freq
        
        for i in range(len(words)):
            word = words[i]
            word_freq = charFreq(word)
            # print(word_freq)
            words[i] = word_freq
        
        ans = []
        # print(words)
        words.sort()
        n = len(words)
        # print(words)
        # print(queries)
        for query in queries:
            res = binarySearch(query,words)
            if words[res] <= query:
                ans.append(n - res - 1)
            else:
                ans.append(n - res)
        return ans
        
            
            
        
        