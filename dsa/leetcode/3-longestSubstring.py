class Solution:

    # Using set
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        left = 0
        seen = set()

        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            max_length = max(max_length, right - left + 1)

        return max_length
    
    # Using hashmap (sliding-window)
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        max_length = 0
        hashmap = {}

        for end in range(len(s)):
            current = s[end]

            if current in hashmap:
                start = max(start, hashmap[current] + 1)

            hashmap[current] = end
            max_length = max(max_length, end - start + 1)

        return max_length