def isPalindrome(string):
    if len(string) == 1 and string[0] == string[-1]:
        return True
    
    if len(string) == 0:
        return False
    
    if string[0] == string[-1]:
        return isPalindrome(string[1:-1])
    return False

print(isPalindrome('niin'))
print(isPalindrome('nitin'))
print(isPalindrome('level'))
print(isPalindrome('nittin'))

    
