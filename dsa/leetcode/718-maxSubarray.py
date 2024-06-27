class Solution:
    def findLength(self, nums1, nums2):
        seen = {}
        n1 = len(nums1)
        for i in range(n1):
            for j in range(i, n1):
                subarray = nums1[i:j + 1]
                string = ''.join(map(str, subarray))
                seen[string] = len(subarray)
        mx = 0
        n2 = len(nums2)
        for i in range(n2):
            for j in range(i, n2):
                subarray = nums2[i:j + 1]
                string = ''.join(map(str, subarray))
                if string in seen:
                    mx = max(seen[string], mx)
        return mx

nums1 = [0,0,0,0,0]
nums2 = [0,0,0,0,0]

s = Solution()
s.findLength(nums1, nums2)

# def print_subarrays(arr):
#     n = len(arr)
#     for i in range(n):  # Starting index of subarray
#         for j in range(i, n):  # Ending index of subarray
#             subarray = arr[i:j + 1]
#             print(subarray)

# # Example usage:
# numbers = [1, 2, 3, 4]
# print_subarrays(numbers)
