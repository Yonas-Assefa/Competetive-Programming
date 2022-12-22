# Enter your code here. Read input from STDIN. Print output to STDOUT
noOfWords = int(input())
wordList = []
for i in range(noOfWords):
    word = input()
    wordList.append(word)

distnictWord = {}
for i in wordList:
    distnictWord[i] = distnictWord.get(i, 0) + 1
print(len(distnictWord))
for i in list(distnictWord.values()):
    print(i, end = " ")
