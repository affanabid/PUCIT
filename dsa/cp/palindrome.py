class Solution:
    def isPalindrome(self, s: str) -> bool:
        sentence = ''
        for char in s:
            if char.isalnum() and not char.isspace():
                sentence += char.lower()
        
        i = 0
        j = len(sentence) - 1
        while i <= j:
            if sentence[i] != sentence[j]:
                return False
            i += 1
            j -= 1
        return True

