class Solution:
    def reverseWords(self, s: str) -> str:
        array = s.split()
        array.reverse()
        return " ".join(array)