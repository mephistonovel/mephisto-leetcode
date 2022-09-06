
# preprocess(str)
# string을 숫자, str단위로 끊어서 리스트로 저장 
# (seperate the string and discern whether each element is a number or not, then make the list of integer, characters, '[',']')
# input: string
# output: list 
# ex. '30[ce]def' -> [30, '[','c','e','[','d','e','f',']'] 
def preprocess(s):
    sep = [] #output을 담은 빈 list
    number = '' #string에서 숫자부분을 인식할 부분 
    for ch in s:
        if ch.isnumeric():
            number += ch #숫자인 부분이 나오면 number에 추가
        else:
            if len(number) > 0: #숫자가 아닌 부분이 나온 상황에서, number 의 length체크 -> 그 length만큼이 숫자가 나온 부분
                sep.append(int(number)) 
                number = '' #해당 숫자를 output sep에 추가한 후, number비우고 초기화
            sep.append(ch) #string input의 char부분은 자동으로 sep에 추가 
    return sep

# decode(s)
# string을 받아 위의 preprocess함수로 list로 바꾼 후, decode 
# input: encoded str
# output: decoded str
def decode(s) -> str:
    NEW_CONTENT_SEP = '_'
    # change string into a list of characters, integers, [, ]
    sep = preprocess(s)

    cursor = len(sep) - 1 # in the loop(process of decoding), specify the position of each element in the list
    content = []  # a text output in reverse order
    
    # loop over the sep in reverse order
    while cursor >= 0:
        if sep[cursor] == '[':
            ...

        elif type(sep[cursor]) == int:
            num = sep[cursor] 
            real_content = '' # to make num * real_content, initialization

            # while loop before the content pops '_'
            while (popped := content.pop()) != NEW_CONTENT_SEP:
                real_content += popped
            content.append(num * real_content) # add num*real_content to content
        elif sep[cursor] == ']':  # 
                content.append(NEW_CONTENT_SEP)
        else:
            content.append(sep[cursor])

        cursor -= 1

    return ''.join(content[::-1])

if __name__ == '__main__':
    tests = ["3[a]2[bc]", "3[a2[c]]", "2[abc]3[cd]ef"]
    for test in tests:
        print(decode(test))


