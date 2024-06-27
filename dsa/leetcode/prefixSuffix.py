class Solution:
    def isPrefixAndSuffix(self, str1, str2):
        len1 = len(str1)
        if len(str1) <= len(str2):
            first = str2[:len1]
            last = str2[-(len1):]
            if first == str1 and last == str1:
                return True
        return False

    def countPrefixSuffixPairs(self, words):
        count = 0
        for i in range(len(words)):
            for j in range(i):
                if self.isPrefixAndSuffix(words[j], words[i]):
                    count += 1
        return count
    
s = Solution()
print(s.isPrefixAndSuffix('aba', 'aa'))
# words = ["a","aba","ababa","aa"]
# words = ["pa","papa","ma","mama"]
words = ["abab","ab"]
print(s.countPrefixSuffixPairs(words))