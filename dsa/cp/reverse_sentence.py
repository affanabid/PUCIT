def reverseSentence(string):
    result = ''
    words = string.split()
    for word in words:
        stack = []
        while word:
            stack.append(word[0])
            word = word[1:]
        while stack:
            result += stack.pop()
        result += ' '
    print(result)
        

reverseSentence('Welcome to DSA')

# s = 'abc'
# while s:
#     print(s[0])
#     s = s[1:]