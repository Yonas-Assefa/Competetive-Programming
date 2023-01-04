word_no = int(input())
word_list = []
for i in range(word_no):
    word = input()
    word_list.append(word)
for word in word_list:
    word = word[:2] + "... " + word + "?"
    print(word)
