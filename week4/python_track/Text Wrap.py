import textwrap

def wrap(string, max_width):
    str_len = len(string)
    new_str = ""
    for i in range(str_len):
        if i % max_width == 0:
            new_str += "\n" + string[i]  
        else:
            new_str += string[i]          
    return new_str.strip()

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)