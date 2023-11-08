class Solution:
    def strStr(self, haystack, needle):
        if needle in haystack: return haystack.index(needle)
        else: return -1

        # return haystack.find(needle)