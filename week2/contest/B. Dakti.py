test_case = int(input())
ans = []
for i in range(test_case):
    chorus = input()
    chorus_list = chorus.split(" ")
    word_dict = {}
    
    for word in chorus_list:
        alpha_word = ""
        for i in word:
            if i.isnumeric():
                num = i
                continue
            else:
                alpha_word += i
                
        word_dict[alpha_word] = num

    sorted_dict = dict(sorted(word_dict.items(),key=lambda kv:kv[1]))
    sorted_list = list(sorted_dict.keys())
    sorted_chorus = " ".join(sorted_list)
    ans.append(sorted_chorus)

for i in ans:
    print(i)
    

