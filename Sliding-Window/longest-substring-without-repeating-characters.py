class Solution:
    def lengthOfLongestSubstring(self, s):
        left, right = 0, 0
        substr, max_length = set(), 0

        while right < len(s):
            if s[right] not in substr:
                substr.add(s[right])
                right += 1
                max_length = max(max_length, (right - left))
            else:
                substr.remove(s[left])
                left += 1

        return max_length

