from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        letters = 'abcdefghijklmnopqrstuvwxyz'
        indices = []
        for l in letters:
            if s.count(l) == 1:
                indices.append(s.index(l))
        if indices:
            return min(indices)
        return -1

