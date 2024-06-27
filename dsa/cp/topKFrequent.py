#from collections import Counter

class Solution:
    def topKFrequent(self, nums, k: int):
        max_num = max(nums)
        b = [0] * (max_num+1)

        for i in range(len(nums)):
            b[nums[i]] += 1   

        freq = []
        i = 0
        while i < k:
            f = (b.index(max(b)))
            # print(type(f))
            freq.append(f)
            b[f] = 0
            i += 1
        print(freq)

n = [1]
s = Solution()
s.topKFrequent(n, 1)
