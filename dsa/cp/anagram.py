class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = sorted(s)
        t = sorted(t)
        return s == t
        #return Counter(s) == Counter(t)
    
s = 'abc'
t = 'abc'
v = Solution()
print(v.isAnagram(s, t))