class Solution:
    def missingNumber(self, nums):
        n = []
        for i in range(len(nums)+1):
            n.append(i)

        for i in nums:
            if i in nums:
                n.remove(i)
        return n[0]