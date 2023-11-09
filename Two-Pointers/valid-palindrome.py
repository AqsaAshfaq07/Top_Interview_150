class Solution:
    def isPalindrome(self, s: str) -> bool:
        # palindrome - reads same forward and backward
        # remove special characters and spaces - just keep alphanumeric characters - .isalnum()
        # remove everything except alpha-numeric characters
        # check if palindrome or not -
        # string == string.reverse()
        # Base Case - empty string - palindrome

       string = ''.join(c for c in s if c.isalnum()).lower()
       return string == string[::-1]